from django.urls import path
from . import views

app_name = 'cocktails'

urlpatterns = [
    # /cocktails/
    path('', views.IndexView.as_view(), name='index'),

    # /cocktails/register
    path('a/registration/', views.UserFormView.as_view(), name='register'),

    # /cocktails/712/
    path('<str:pk>/', views.DetailView.as_view(), name='detail'),

    # /cocktails/cocktail/add/
    #path('cocktail/add/', views.CocktailCreate.as_view(), name='cocktail-add'),

    # /cocktails/cocktail/2/
    path('cocktail/<str:pk>/', views.CocktailUpdate.as_view(), name='cocktail-update'),

    # cocktails/cocktail/2/delete
    path('cocktail/<str:pk>/delete', views.CocktailDelete.as_view(), name='cocktail-delete'),

    # /cocktails/<cocktail_name>/favorite
    path('<str:cocktail_name>/favorite_cocktail/', views.favorite_cocktail, name='favorite_cocktail'),
]
