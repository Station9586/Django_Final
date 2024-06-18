"""
URL configuration for final project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from main import views
import member.views as member

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login), 
    path('register/', views.register),
    # path('main/<str:no>/', views.main, name='page'),
    path('main/pg1/', member.main), 
    path('main/pg2/', member.showdata),
    path('main/pg2/delete/<str:id>', member.detete_r, name='del-url'),
    path('main/pg3/', member.go_reserve2),
    path('main/pg4/', member.modify),
    path('main/pg5/', member.settings),
    path('main/pg5/delete/<str:old_psw>/', member.delete),
    path('main/logout/', member.logout),
    re_path(r"^captcha/", include("captcha.urls")), 
    path("accounts/", include("registration.backends.default.urls")), 
]
