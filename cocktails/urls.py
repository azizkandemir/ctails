from django.urls import path
from . import views


app_name = 'cocktails'

urlpatterns = [
    # /cocktails/
    path('', views.IndexView.as_view(), name='index'),

    # /cocktails/712/
    path('<str:pk>/', views.DetailView.as_view(), name='detail'),

    # /cocktails/<cocktail_name>/favorite
    #path('<str:cocktail_name>/favorite/', views.favorite, name='favorite'),
]
