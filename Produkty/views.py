from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *


def rejestracja(request):
    form = NowyUzytkownikForm()

    if request.method == 'POST':
        form = NowyUzytkownikForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Konto zostało stworzone.')
            return redirect('logowanie')

    dane = {'form': form}
    return render(request, 'rejestracja.html', dane)


def logowanie(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')

        dane = {'user': user}
        return render(request, 'logowanie.html', dane)
    else:
        dane = {}
        return render(request, 'logowanie.html', dane)


@login_required
def wyloguj(request):
    logout(request)
    return HttpResponseRedirect(reverse('strona_glowna'))

def koszyk(request):
    obecny_uzytkownik = request.user.id
    przedmioty_w_koszyku = Koszyk_Przedmioty.objects.filter(cart=obecny_uzytkownik)
    dane = {'obecny_uzytkownik':obecny_uzytkownik,'przedmioty_w_koszyku':przedmioty_w_koszyku}
    return render(request,'koszyk.html',dane)





@login_required
def mojekonto(request):
    if request.user.is_authenticated:
        obecny_uzytkownik = request.user.id
        zakupy = Historia_zakupów.objects.filter(user=obecny_uzytkownik)
        dane = {'obecny_uzytkownik': obecny_uzytkownik,'zakupy':zakupy}
        return render(request, 'mojekonto.html', dane)


def index(request):
    kategorie = Kategoria.objects.all()
    dane = {'kategorie': kategorie}
    return render(request, 'index.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    dane = {'kategoria_user': kategoria_user, 'kategoria_produkt': kategoria_produkt, 'kategorie': kategorie}
    return render(request, 'kategoria.html', dane)


def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)


def dodaj_do_koszyka(request, id):

    if request.user.is_authenticated:
        if request.method == 'GET':
            obecny_uzytkownik = request.user
            obecny_koszyk = Koszyk.objects.get(user=obecny_uzytkownik)
            przedmiot = Produkty.objects.get(pk=id)
            przedmiot_w_koszyku = None
            try:
                przedmiot_w_koszyku = Koszyk_Przedmioty.objects.get(przedmiot=przedmiot, cart=obecny_koszyk)
            except:
                pass
            

            if przedmiot_w_koszyku != None:
                przedmiot_w_koszyku.ilosc += 1
                przedmiot_w_koszyku.save()
                return HttpResponseRedirect(reverse('strona_glowna'))

            else:
                koszyk = Koszyk_Przedmioty(przedmiot=przedmiot,ilosc=1,cart=obecny_koszyk)
                koszyk.save()
                return HttpResponseRedirect(reverse('strona_glowna'))




def usun_z_koszyka(request, id):

    if request.method == 'GET':
        obecny_uzytkownik = request.user
        obecny_koszyk = Koszyk.objects.get(user=obecny_uzytkownik)
        przedmiot = Produkty.objects.get(pk=id)
        przedmiot_w_koszyku = Koszyk_Przedmioty.objects.get(przedmiot=przedmiot, cart=obecny_koszyk)
           

        if przedmiot_w_koszyku:
            przedmiot_w_koszyku.delete()
            return HttpResponseRedirect(reverse('koszyk'))

def kup_teraz(request, id):
    if request.method == 'GET':
        obecny_uzytkownik = request.user.id
        obecny_koszyk = Koszyk.objects.get(user=obecny_uzytkownik)
        #przedmiot = Produkty.objects.get(pk=0)
        przedmioty_w_koszyku = Koszyk_Przedmioty.objects.filter(cart=obecny_koszyk)
        lst = []
        

           
        if obecny_koszyk:
            for p in przedmioty_w_koszyku:
                przedmiot = Produkty.objects.get(nazwa=p.przedmiot)

                dodawanie = Historia_zakupów(user=obecny_koszyk,ilosc = p.ilosc,  przedmiot=przedmiot)
                dodawanie.save()

        przedmioty_w_koszyku.delete()
        return HttpResponseRedirect(reverse('mojekonto'))







