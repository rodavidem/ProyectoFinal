"""
URL configuration for ProyectoFinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from . import views
from .views import AdminView, ListaDiscosView, EditarDiscoView, BorrarDiscoView, DiscoDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("template/", views.template, name="template"),
    path('submit-contact/', views.contact_submit, name='contact_submit'),
    path('buscar/', views.buscar, name='buscar'),
    path('resultados/', views.resultados, name='resultados'),
    path('signup/', views.authView, name='signup'),
    path("accounts/", include('django.contrib.auth.urls')),
    path('adminview/', AdminView.as_view(), name='admin_view'),
    path('lista/', ListaDiscosView.as_view(), name='lista'),
    path('editar_disco/<int:pk>/', EditarDiscoView.as_view(), name='editar_disco'),
    path('borrar_disco/<int:pk>/', BorrarDiscoView.as_view(), name='borrar_disco'),
    path('pages/<int:pk>/', DiscoDetailView.as_view(), name='disco_detalle'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)