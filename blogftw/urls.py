from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('blog/', include('blog.urls')),
    path('better_auth/', include('better_auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

]