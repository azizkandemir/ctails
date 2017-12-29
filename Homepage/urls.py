from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'Homepage'

urlpatterns = [
    # /Homepage
    path('', views.index, name='index'),
    path('login', auth_views.login, {'template_name': 'Homepage/login.html'}, name='login'),
    path('logout', auth_views.logout, {'template_name': 'Homepage/logout.html'}, name='logout'),
]
