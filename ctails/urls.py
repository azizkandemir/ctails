from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cocktails/', include('cocktails.urls')),
    path('', include('Homepage.urls')),
]
