"""Sklep URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from Produkty.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='strona_glowna'),
    path('rejestracja', rejestracja, name='rejestracja'),
    path('logowanie', logowanie, name='logowanie'),
    path('kategoria/<id>/', kategoria, name="kategoria"),
    path('produkt/<id>/', produkt, name="produkt"),
    path('wyloguj', wyloguj, name='wyloguj'),
    path('mojekonto', mojekonto, name='mojekonto'),
    path('koszyk',koszyk,name='koszyk'),
    path('produkt/<id>/dodaj_do_koszyka', dodaj_do_koszyka, name='dodaj_do_koszyka'),
    path('koszyk/<id>/', usun_z_koszyka, name='usun_z_koszyka'),
    path('kup_teraz/<id>',kup_teraz,name='kup_teraz'),
]

