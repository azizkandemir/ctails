from django.urls import path
from . import views

app_name = 'usercocktails'

urlpatterns = [
    # /usercocktails/
    path('', views.IndexView.as_view(), name='index'),

    # /cocktails/712/
    path('<str:pk>/', views.DetailView.as_view(), name='detail'),

    # /cocktails/cocktail/add/
    path('usercocktails/add/', views.CocktailCreate.as_view(), name='cocktail-add'),

    # /cocktails/cocktail/2/
    path('usercocktails/<str:pk>/', views.CocktailUpdate.as_view(), name='cocktail-update'),

    # cocktails/cocktail/2/delete
    path('usercocktails/<str:pk>/delete', views.CocktailDelete.as_view(), name='cocktail-delete'),

    # /cocktails/<cocktail_name>/favorite
    path('<str:cocktail_name>/favorite_cocktail/', views.favorite_cocktail, name='favorite_cocktail'),
]