from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import *
from .models import *

# @login_required
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
    hunts_count = Hunting.objects.filter(user=request.user).count()
    fish_count = Fishing.objects.filter(user=request.user).count()
    photos_count = Post.objects.filter(user=request.user).count()

    context = {
        'hunts_count': hunts_count,
        'fish_count': fish_count,
        'photos_count': photos_count,
    }
    return render(request, "base.html", context)

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
            log = form.save(commit=False)
             

            if "picture" in request.FILES:
                log.picture = request.FILES["picture"]

            messages.success(request, "Hunting log updated successfully.")
            return redirect("hunting")

    else:
        form = HuntingForm(instance=edit_hunt)

    return render(request, "loghunt.html", {
        "form": form,
        "edit": True,
        "log": edit_hunt,  
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
            log = form.save(commit=False)
            

            
            if "picture" in request.FILES:
                log.picture = request.FILES["picture"]

            messages.success(request, "Fishing log updated successfully.")
            return redirect("fishing")

    else:
        form = FishingForm(instance=edit_fish)

    return render(request, "logfish.html", {
        "form": form,
        "edit": True,
        "log": edit_fish,
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
    
def is_admin(user):
    return user.is_authenticated and user.is_superuser

def admin_login(request):
    if request.user.is_authenticated and request.user.is_superuser:
        return redirect('admin_dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user and user.is_superuser:
            login(request, user)
            return redirect('admin_dashboard')

        return render(request, 'Login_sign_up', {
            'error': 'Invalid admin credentials'
        })

    return render(request, "Login_sign_up")

@login_required
def admin_logout(request):
    logout(request)
    return redirect('Login_sign_up')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):

    if not request.user.is_superuser:
        return redirect("home")

    context = {
        "user_count": User.objects.count(),
        "post_count": Post.objects.count(),
        "hunting_count": Hunting.objects.count(),
        "fishing_count": Fishing.objects.count(),
        "users": User.objects.all().order_by("username"),
        "posts": Post.objects.all().order_by("-date"),
    }
    return render(request, "admin.html", context)

@login_required
def admin_create_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        is_staff = request.POST.get('is_staff') == 'on'
        is_superuser = request.POST.get('is_superuser') == 'on'

        if User.objects.filter(username=username).exists():
            return render(request, 'Login_sign_up', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.save()

        return redirect('admin_users')

    return render(request, 'Login_sign_up')

@login_required
def admin_edit_user(request, user_id):

    if not request.user.is_superuser:
        return redirect("home")

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.username = request.POST.get('username')
        user.email = request.POST.get('email')

        if user != request.user: 
            user.is_staff = request.POST.get('is_staff') == 'on'
            user.is_superuser = request.POST.get('is_superuser') == 'on'
            user.is_active = request.POST.get('is_active') == 'on'
            user.save()

        user.save()
        messages.success(request, "User updated successfully.")
        return redirect('admin_dashboard')

    return render(
        request,
        'admin_panel/edit_user.html',
        {'user': user}
    )
@login_required
@user_passes_test(is_admin)
def admin_change_password(request, user_id):
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        password = request.POST.get('password')
        user.set_password(password)
        user.save()

        return redirect('admin_users')

    return render(request, 'Login_sign_up', {'user': user})

@login_required
@user_passes_test(is_admin)
def admin_delete_user(request, user_id):

    if not request.user.is_superuser:
        return redirect("home")

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        user.delete()
        return redirect('admin_users')

    return render(request, 'Login_sign_up', {'user': user})

@login_required
def admin_post_list(request):
    posts = Post.objects.select_related('user').all().order_by('-id')
    return render(request, 'admin_panel/posts.html', {'posts': posts})

@login_required
def admin_edit_post(request, post_id):
    if not request.user.is_superuser:
        return redirect("home")
     
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.location = request.POST.get('location')
        post.description = request.POST.get('description')
        post.quantity = request.POST.get('quantity') or 0

        if request.FILES.get("picture"):
            post.picture = request.FILES['picture']

        post.save()
        
        messages.success(request, "Post updated successfully.")
        return redirect('admin_dashboard')

    return render(request, 'admin_panel/edit_post.html', {'post': post})

@login_required
@user_passes_test(is_admin)
def admin_delete_post(request, post_id):

    if not request.user.is_superuser:
        return redirect("home")
    
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post.delete()
        return redirect('admin_posts')

    return render(request, 'admin_panel/confirm_delete_post.html', {'post': post})
