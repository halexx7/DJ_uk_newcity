from mainapp.models import Appartament, UserProfile
from django.conf import settings
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.views.generic.detail import DetailView
from django.forms.models import BaseInlineFormSet, inlineformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin

from authnapp.forms import UserEditForm, UserLoginForm, UserRegisterForm, BaseChildrenFormset, AppartamentEditForm, UserProfileEditForm
from authnapp.models import User


def login(request):
    title = "Вход | УК \"Новый город\""

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
    title = "Регистрация | УК \"Новый город\""

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


# @login_required
# @transaction.atomic
# def edit(request):
#     title = "Редактирование | УК \"Новый город\""

#     if request.method == "POST":
#         edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
#         profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
#         if edit_form.is_valid() and profile_form.is_valid():
#             edit_form.save()
#             return HttpResponseRedirect(reverse("auth:edit"))
#     else:
#         edit_form = UserEditForm(instance=request.user)
#         profile_form = UserProfileEditForm(instance=request.user.userprofile)

#     content = {"title": title, "edit_form": edit_form, "profile_form": profile_form, "media_url": settings.MEDIA_URL}

#     return render(request, "authnapp/edit.html", content)


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


class UsersUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = "authnapp/edit.html"
    success_url = reverse_lazy("admin:edit")
    form_class = UserEditForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "пользователи/редактирование"
        # context["appartament"] = AppartamentEditForm(instance=self.request.user.profiles)
        # context['profile_form'] = UserProfileEditForm(instance=self.request.user.profiles)

        UserProfileFormSet = inlineformset_factory(User, UserProfile, form=BaseChildrenFormset, extra=1)

        if self.request.POST:
            context["appartament"] = UserProfileFormSet(self.request.POST, instance=self.object)
        else:
            # queryset = self.object.profiles
            queryset = get_object_or_404(User, id=self.object.id)
            formset = UserProfileFormSet(instance=queryset)
            context["appartament"] = formset
        return context

# #TODO Переделать под себя
# class UserUpdate(UpdateView):
#     model = User
#     fields = []
#     template_name = 'authnapp/edit.html'
#     success_url = reverse_lazy("main")

#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         data['user'] = self.request.user
#         # data['title'] = "редактирование"
#         data['profile_form'] = UserProfileEditForm(instance=self.request.user.profiles)
#         UserProfileFormSet = inlineformset_factory(User, UserProfile, form=BaseChildrenFormset, extra=1)
       
#         if self.request.POST:
#             data["appartament"] = UserProfileFormSet(self.request.POST, instance=self.object)
#         else:
#             queryset = self.object.profiles.select_related()
#             formset = UserProfileFormSet(instance=self.object, queryset=queryset)
#             data["appartament"] = formset
#         return data

    # def form_valid(self, form):
    #     context = self.get_context_data()
    #     # orderitems = context["orderitems"]

    #     with transaction.atomic():
    #         self.object = form.save()
    #         if orderitems.is_valid():
    #             orderitems.instance = self.object
    #             orderitems.save()

    #     # Delete empty order
    #     if self.object.get_total_cost() == 0:
    #         self.object.delete()

    #     return super(OrderItemsUpdate, self).form_valid(form)
