from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.contrib.auth import views as better_auth
from . import views

app_name = "better_auth"
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.register, name='register'),
    path('register', views.register, name='register'),
    path('user_page', views.user_page, name='user_page'),
    path('login', views.login, name="login"),
]