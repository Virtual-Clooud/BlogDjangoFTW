from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views

app_name = "blog"

urlpatterns = [
    path('create_blog', views.CreateBlog, name="create_blog"),
    path('', views.BlogView, name='blog_view'),
    path('<int:post_id>', views.PostDetail, name='post_detail'),
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
]