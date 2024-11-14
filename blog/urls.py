from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from django.urls import path, include
from blog.views import blog_home, blog_detail, about_me, blog_category

urlpatterns = [
    path('post/<int:id>/', blog_detail, name='blog_detail'),
    path('about/',about_me, name='about'),
    path('', blog_home, name='home'),
    path('category/<category>', blog_category, name='blog_category'),
  
    
]
