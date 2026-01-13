"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_signup, name="Login_sign_up"),
    path("logout/", logout_view, name="logout"),
    path("home/", home_page, name="home"),
    path("hunting/",hunting_page, name="hunting"),
    path("fishing/", fishing_page, name="fishing"),
    path("photo/", photo_page, name="photo"),
    path("post/", create_post, name="post"),
    path("hunting_log/", hunting_log, name="loghunt" ),
    path("fishing_log/", fishing_log, name="logfish" ),
    path("hunting/delete/<int:id>/", delete_hunting_log, name="delete_hunt"),
    path("hunting/edit/<int:id>/", edit_hunting_log, name="edit_hunt"),
    path("fishing/delete/<int:id>/", delete_fishing_log, name="delete_fish"),
    path("fishing/edit/<int:id>/", edit_fishing_log, name="edit_fish"),
    path("post/edit/<int:id>/", edit_post, name="edit_post"),
    path("post/delete/<int:id>/", delete_post, name="delete_post"),


    
] 

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )

