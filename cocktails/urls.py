from django.urls import path
from . import views

urlpatterns = [
    # /cocktails/
    path('', views.index, name='index'),

    # /cocktails/712/
    path('<str:cocktail_name>/', views.detail, name='detail'),
]
