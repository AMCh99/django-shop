from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
from django.contrib.auth import get_user_model


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"

def post_save_profile_create(sender, instance, created, *args, **kwargs):
    if created:
        Profil.objects.get_or_create(user=instance)

post_save.connect(post_save_profile_create, sender=settings.AUTH_USER_MODEL)


class Producent(models.Model):
    nazwa_producenta = models.CharField(max_length=50)

    def __str__(self):
        return self.nazwa_producenta

    class Meta:
        verbose_name = "Producent"
        verbose_name_plural = "Producenci"


class Kategoria(models.Model):
    kategoria_produktu = models.CharField(max_length=50)

    def __str__(self):
        return self.kategoria_produktu

    class Meta:
        verbose_name = "Kategoria"
        verbose_name_plural = "Kategorie"


class Produkty(models.Model):
    nazwa = models.CharField(max_length=50)
    producent = models.ForeignKey(Producent, on_delete=models.CASCADE, null=True)
    kategoria = models.ForeignKey(Kategoria, on_delete=models.CASCADE, null=True)
    opis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nazwa

    class Meta:
        verbose_name = "Produkt"
        verbose_name_plural = "Produkty"


class Koszyk(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return self.user.username


    class Meta:
        verbose_name = "Koszyk"
        verbose_name_plural = "Koszyki"


def post_save_koszyk_create(sender, instance, created, *args, **kwargs):
    if created:
        Koszyk.objects.get_or_create(user=instance)

post_save.connect(post_save_koszyk_create, sender=settings.AUTH_USER_MODEL)


class Koszyk_Przedmioty(models.Model):
    przedmiot = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    ilosc = models.IntegerField(default=1)
    cart = models.ForeignKey(Koszyk, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.cart) + ' -- ' + str(self.przedmiot)

    class Meta:
        verbose_name = "Przedmioty w Koszyku"
        verbose_name_plural = "Przedmioty w Koszykach"


class Historia_zakupów(models.Model):
    user = models.ForeignKey(Koszyk, on_delete=models.CASCADE)
    przedmiot = models.ForeignKey(Produkty, on_delete=models.CASCADE)
    ilosc = models.IntegerField(default=1)
    data_zakupu = models.DateField(auto_now_add=True)
        
    class Meta:
        verbose_name = "Historia_zakupów"
        verbose_name_plural = "Historia_zakupów"


