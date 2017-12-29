from django.urls import path
from . import views

app_name = 'what2drink'

urlpatterns = [
    # /what2drink
    path('', views.IndexView.as_view(), name='index'),
    path('<str:pk>', views.IndexView2.as_view(), name='vodka'),
    path('<str:pk>', views.IndexView3.as_view(), name='tequila'),
    path('<str:pk>', views.IndexView4.as_view(), name='gin'),
    path('<str:pk>', views.IndexView5.as_view(), name='rom'),
    path('<str:pk>', views.IndexView6.as_view(), name='triple sec'),
]
