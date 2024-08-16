from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("ProyectoFinal.urls")),
    path("accounts/", include('django.contrib.auth.urls')),
]