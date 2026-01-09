from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages



def login_signup(request):
    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "login":
            username = request.POST.get("username")
            password = request.POST.get("password")

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password")
                return redirect("Login_sign_up")

        if form_type == "signup":
            username = request.POST.get("username")
            password = request.POST.get("password1")
            email = request.POST.get("email")

            if User.objects.filter(username=username).exists():
                return render(request, "login.html", {
                    "error": "Username already exists"
                })
             
            user = User.objects.create_user(
                username=username,
                password=password,
                email=email
            )
            login(request, user)
            return redirect("home")

    return render(request, "login.html")


def home_page(request):
    return render(request, "base.html")


































































