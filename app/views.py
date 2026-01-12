from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *


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

@login_required
def hunting_page(request):
    hunting = Hunting.objects.filter(user=request.user)
    return render(request, "hunting.html", {"hunting": hunting})

def hunting_log(request):
    if request.method == "POST":
        form = HuntingForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            
            return redirect("hunting")

    
    else:
        form = HuntingForm()

    
    return render(request, "loghunt.html", {"form": form})

@login_required
def fishing_page(request):
    fishing = Fishing.objects.filter(user=request.user)
    return render(request, "fishing.html", {"fishing": fishing})

def fishing_log(request):
    if request.method == "POST":
        form = FishingForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            
            return redirect("fishing")

    
    else:
        form = FishingForm()

    
    return render(request, "logfish.html", {"form": form})

def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

            
            return redirect("photo")

    
    else:
        form = PostForm()

    
    return render(request, "create_post.html", {"form": form})

@login_required
def photo_page(request):
    posts = Post.objects.all().order_by('-date')
    return render(request, "photo.html", {"posts": posts})



































































