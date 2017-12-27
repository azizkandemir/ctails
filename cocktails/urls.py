from django.urls import path
from . import views


app_name = 'cocktails'

urlpatterns = [
    # /cocktails/
    path('', views.index, name='index'),

    # /cocktails/712/
    path('<str:cocktail_name>/', views.detail, name='detail'),

    # /cocktails/<cocktail_name>/favorite
    path('<str:cocktail_name>/favorite/', views.favorite, name='favorite'),
]
