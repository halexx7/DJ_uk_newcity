from django.conf import settings
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from apps.authnapp.forms import (ProfileFormset, UserEditForm, UserLoginForm,
                            UserRegisterForm)
from apps.authnapp.models import User


def login(request):
    title = 'Вход | УК "Новый город"'

    login_form = UserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        personal_account = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(personal_account=personal_account, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main"))

    content = {"title": title, "form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = 'Регистрация | УК "Новый город"'

    if request.method == "POST":
        register_form = UserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print("сообщение для подтверждения регистрации отправлено")
                return HttpResponseRedirect(reverse("auth:login"))
            print("ошибка отправки сообщения для подтверждения регистрации")
            return HttpResponseRedirect(reverse("auth:login"))
    else:
        register_form = UserRegisterForm()

    content = {"title": title, "register_form": register_form}
    return render(request, "authnapp/register.html", content)


def send_verify_mail(user):
    verify_link = reverse("auth:verify", args=[user.email, user.activation_key])

    title = f"Подтверждение учетной записи {user.personal_account}"
    message = f"Для подтверждения учетной записи {user.personal_account} \
    на портале {settings.DOMAIN_NAME} перейдите по ссылке: \
    \n{settings.DOMAIN_NAME}{verify_link}"

    print(f"from: {settings.EMAIL_HOST_USER}, to: {user.email}")
    return send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
    )


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            print(f"user {user} is activated")
            user.is_active = True
            user.save()
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")

            return render(request, "authnapp/verification.html")
        print(f"error activation user: {user}")
        return render(request, "authnapp/verification.html")

    except Exception as e:
        print(f"error activation user : {e.args}")

    return HttpResponseRedirect(reverse("main"))


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "authnapp/edit.html"
    success_url = reverse_lazy("main")
    form_class = UserEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context["profile_form"] = ProfileFormset(self.request.POST, instance=self.object)
        else:
            context["profile_form"] = ProfileFormset(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = ProfileFormset(self.request.POST, instance=self.object)

        if not self.request.user.is_staff:
            if form.is_valid() and formset.is_valid():
                return self.form_valid(form, formset)
            return self.form_invalid(form, formset)
        else:
            if form.is_valid():
                return self.form_valid(form, formset)

    def form_valid(self, form, formset):
        if self.request.user.is_staff:
            self.object = form.save()
        else:
            with transaction.atomic():
                self.object = form.save()
                formset.instance = self.object
                formset.save()

        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form, formset):
        return self.render_to_response(
            self.get_context_data(
                form=form,
                appartament_form=formset,
            )
        )
