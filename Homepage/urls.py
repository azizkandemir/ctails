from django.urls import path
from . import views

app_name = 'Homepage'

urlpatterns = [
    # /Homepage
    path('', views.index, name='index'),
]
