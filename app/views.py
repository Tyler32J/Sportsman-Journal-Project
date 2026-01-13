from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *

@login_required
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

def logout_view(request):
    logout(request)
    return redirect("Login_sign_up")

@login_required
def home_page(request):
    return render(request, "base.html")

@login_required
def hunting_page(request):
    hunting = Hunting.objects.filter(user=request.user)
    return render(request, "hunting.html", {"hunting": hunting})

@login_required
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
def delete_hunting_log(request, id):
    delete_hunt_log = get_object_or_404(Hunting, id=id, user=request.user)
    if request.method == "POST":
        delete_hunt_log.delete()
        messages.success(request, "Hunting log deleted successfully.")
        return redirect("hunting")

@login_required
def edit_hunting_log(request, id):
    edit_hunt = get_object_or_404(Hunting, id=id, user=request.user)

    if request.method == "POST":
        form = HuntingForm(request.POST, request.FILES, instance=edit_hunt)

        if form.is_valid():
            form.save()
            messages.success(request, "Hunting log updated successfully.")
            return redirect("hunting")

    else:
        form = HuntingForm(instance=edit_hunt)

    return render(request, "loghunt.html", {
        "form": form,
        "edit": True
    })

@login_required
def fishing_page(request):
    fishing = Fishing.objects.filter(user=request.user)
    return render(request, "fishing.html", {"fishing": fishing})

@login_required
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

@login_required
def delete_fishing_log(request, id):
    delete_fish_log = get_object_or_404(Fishing, id=id, user=request.user)
    if request.method == "POST":
        delete_fish_log.delete()
        messages.success(request, "Fishing log deleted successfully.")
        return redirect("fishing")

@login_required
def edit_fishing_log(request, id):
    edit_fish = get_object_or_404(Fishing, id=id, user=request.user)

    if request.method == "POST":
        form = FishingForm(request.POST, request.FILES, instance=edit_fish)

        if form.is_valid():
            form.save()
            messages.success(request, "Fishing log updated successfully.")
            return redirect("fishing")

    else:
        form = FishingForm(instance=edit_fish)

    return render(request, "logfish.html", {
        "form": form,
        "edit": True
    })

@login_required
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

@login_required
def edit_post(request, id):
    edit_post = get_object_or_404(Post, id=id, user=request.user)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=edit_post)

        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully.")
            return redirect("photo")

    else:
        form = PostForm(instance=edit_post)

    return render(request, "create_post.html", {
        "form": form,
        "edit": True
    })

@login_required
def delete_post(request, id):
    delete_post = get_object_or_404(Post, id=id, user=request.user)
    if request.method == "POST":
        delete_post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("photo")



































































