"""HDP115 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from flujoMigratorio.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from flujoMigratorio import views 
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index.as_view(), name='home'),
    path('accounts/login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('registrarPersona/',registrarPersona.as_view(), name='registrarPersona'),
    path('buscarPersonaEntrada/',indexEntrarPersona.as_view(),name='buscarPersonaEntrada'),
    path('registrarEntradaPersona/<str:idp>/',entradaPersona.as_view(),name='registrarEntradaPersona'),
    path('indexPersonas/',indexPersonas.as_view(),name='indexPersonas'),
    path('agregarAlarma/<str:idp>/',agregarAlarma.as_view(),name='agregarAlarma'),
    path('buscarPersonaSalida/',indexSalirPersona.as_view(),name='buscarPersonaSalida'),
    path('registrarSalidaPersona/<str:idp>/',salidaPersona.as_view(),name='registrarSalidaPersona')
]

