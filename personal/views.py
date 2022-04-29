from urllib import request
from django.shortcuts import render

def personal(request):
    return render(request,'personal.html')

def belgetalebi(request):
    return render(request,'belge.html')

def hak(request):
    return render(request,'hak.html')

def iban(request):
    return render(request,'iban.html')

def ders(request):
    return render(request,'ders.html')

def yeni_kayit(request):
    return render(request,'yeni_kayit.html')

def ilk_kayit(request):
    return render(request,'ilk_kayit.html')

def yabanci(request):
    return render(request,'yabanci.html')

def dikey(request):
    return render(request,'dikey.html')

def katki(request):
    return render(request,'katki.html')

def anket(request):
    return render(request,'anket.html')

def notgorme(request):
    return render(request,'notgorme.html')

def devamsizlik(request):
    return render(request,'devamsizlik.html')

def nott(request):
    return render(request,'not.html')

def mesaj(request):
    return render(request,'mesaj.html')