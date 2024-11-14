
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('control/', admin.site.urls),
    path('', include('blog.urls')), 
    path("__reload__/", include("django_browser_reload.urls")),
]
    
