# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Account

# Create your views here.


def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=email)
        if not user.exists():
            messages.warning(request, f"Account does not exist")
            return HttpResponseRedirect(request.path_info)

        if not user[0].account.email_verified:
            messages.warning(request, "Account not verified, Please check your email!")
            return HttpResponseRedirect(request.path_info)

        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect("index")

        messages.warning(request, "Invalid Details")

    template_name = "accounts/login.html"
    context = {}
    return render(request, template_name, context)


def register_view(request):
    if request.method == "POST":
        first_name = request.POST.get("first-name")
        last_name = request.POST.get("last-name")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(username=email)
        if user.exists():
            messages.warning(request, f"This email is already in use")
            return HttpResponseRedirect(request.path_info)

        user = User.objects.create(
            first_name=first_name, last_name=last_name, email=email, username=email
        )
        user.set_password(password)
        user.save()
        messages.success(request, "An Email has been sent on your mail.")
        return redirect("login")

    template_name = "accounts/register.html"
    context = {}
    return render(request, template_name, context)


def activate_email(request, email_token):
    try:
        user = Account.objects.get(email_token=email_token)
        user.email_verified = True
        user.save()
    except Exception as e:
        messages.warning(request, f"Invalid Email Token")
        return redirect("login")

    return redirect("index")


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect("index")
