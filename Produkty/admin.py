from django.contrib import admin
from .models import *

class Options_prod(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['nazwa']}),
        ('Produkty', {'fields': ['Producent', 'Kategoria']
             ,'classes': ['collapse']}), ]

    list_display = ('nazwa', 'cena', 'kategoria','producent')
    list_filter = ['kategoria', 'producent']


class Options_kosz(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['przedmiot']}),
        ('Koszyk', {'fields': ['cart']
            , 'classes': ['collapse']}), ]

    list_display = ('przedmiot', 'cart', 'ilosc')
    list_filter = ['cart']


class Options_his(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['przedmiot']}),
        ('Profil', {'fields': ['user']
            , 'classes': ['collapse']}), ]

    list_display = ('przedmiot', 'user', 'ilosc','data_zakupu')
    list_filter = ['user']


admin.site.register(Produkty,Options_prod)
admin.site.register(Producent)
admin.site.register(Kategoria)
admin.site.register(Profil)
admin.site.register(Koszyk)
admin.site.register(Koszyk_Przedmioty, Options_kosz)
admin.site.register(Historia_zakupów, Options_his)
