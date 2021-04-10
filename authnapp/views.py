from django.contrib import auth
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse

from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction
from django.contrib.auth.decorators import login_required


from authnapp.forms import UserEditForm, UserLoginForm, UserProfileEditForm, UserRegisterForm
from authnapp.models import User


def login(request):
    title = "вход"

    login_form = UserLoginForm(data=request.POST or None)
    if request.method == "POST" and login_form.is_valid():
        personal_account = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(personal_account=personal_account, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("main"))

    content = {"title": title, "login_form": login_form}
    return render(request, "authnapp/login.html", content)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("main"))


def register(request):
    title = "регистрация"

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


@login_required
@transaction.atomic
def edit(request):
    title = "редактирование"

    if request.method == "POST":
        edit_form = UserEditForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileEditForm(request.POST, instance=request.user.userprofile)
        if edit_form.is_valid() and profile_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse("auth:edit"))
    else:
        edit_form = UserEditForm(instance=request.user)
        profile_form = UserProfileEditForm(instance=request.user.userprofile)

    content = {"title": title, "edit_form": edit_form, "profile_form": profile_form, "media_url": settings.MEDIA_URL}

    return render(request, "authnapp/edit.html", content)


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