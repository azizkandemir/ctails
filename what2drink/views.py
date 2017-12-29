from django.shortcuts import render
from django.views import generic
from cocktails.models import Spirit, Cocktail

class IndexView(generic.ListView):
    template_name = 'what2drink/index.html'
    context_object_name = 'all_spirits'

    def get_queryset(self):
        return Spirit.objects.all()

class IndexView2(generic.ListView):
    template_name = 'what2drink/vodka.html'
    context_object_name = 'vodka_cocktails'

    def get_queryset(self):
        if Cocktail.objects.all().filter(spirit1__startswith='V'):
            return Cocktail.objects.all().filter(spirit1__startswith='V')
        if Cocktail.objects.all().filter(spirit2__startswith='V'):
            return Cocktail.objects.all().filter(spirit2__startswith='V')
        if Cocktail.objects.all().filter(spirit3__startswith='V'):
            return Cocktail.objects.all().filter(spirit3__startswith='V')
        if Cocktail.objects.all().filter(spirit4__startswith='V'):
            return Cocktail.objects.all().filter(spirit4__startswith='V')
        if Cocktail.objects.all().filter(spirit5__startswith='V'):
            return Cocktail.objects.all().filter(spirit5__startswith='V')


class IndexView3(generic.ListView):
    template_name = 'what2drink/tequila.html'
    context_object_name = 'tequila_cocktails'

    def get_queryset(self):
        if Cocktail.objects.all().filter(spirit1__startswith='Te'):
            return Cocktail.objects.all().filter(spirit1__startswith='Te')
        if Cocktail.objects.all().filter(spirit2__startswith='Te'):
            return Cocktail.objects.all().filter(spirit2__startswith='Te')
        if Cocktail.objects.all().filter(spirit3__startswith='Te'):
            return Cocktail.objects.all().filter(spirit3__startswith='Te')
        if Cocktail.objects.all().filter(spirit4__startswith='Te'):
            return Cocktail.objects.all().filter(spirit4__startswith='Te')
        if Cocktail.objects.all().filter(spirit5__startswith='Te'):
            return Cocktail.objects.all().filter(spirit5__startswith='Te')

class IndexView4(generic.ListView):
    template_name = 'what2drink/gin.html'
    context_object_name = 'gin_cocktails'

    def get_queryset(self):
        if Cocktail.objects.all().filter(spirit1__startswith='G'):
            return Cocktail.objects.all().filter(spirit1__startswith='G')
        if Cocktail.objects.all().filter(spirit2__startswith='G'):
            return Cocktail.objects.all().filter(spirit2__startswith='G')
        if Cocktail.objects.all().filter(spirit3__startswith='G'):
            return Cocktail.objects.all().filter(spirit3__startswith='G')
        if Cocktail.objects.all().filter(spirit4__startswith='G'):
            return Cocktail.objects.all().filter(spirit4__startswith='G')
        if Cocktail.objects.all().filter(spirit5__startswith='G'):
            return Cocktail.objects.all().filter(spirit5__startswith='G')

class IndexView5(generic.ListView):
    template_name = 'what2drink/rom.html'
    context_object_name = 'rom_cocktails'

    def get_queryset(self):
        if Cocktail.objects.all().filter(spirit1__startswith='R'):
            return Cocktail.objects.all().filter(spirit1__startswith='R')
        if Cocktail.objects.all().filter(spirit2__startswith='R'):
            return Cocktail.objects.all().filter(spirit2__startswith='R')
        if Cocktail.objects.all().filter(spirit3__startswith='R'):
            return Cocktail.objects.all().filter(spirit3__startswith='R')
        if Cocktail.objects.all().filter(spirit4__startswith='R'):
            return Cocktail.objects.all().filter(spirit4__startswith='R')
        if Cocktail.objects.all().filter(spirit5__startswith='R'):
            return Cocktail.objects.all().filter(spirit5__startswith='R')

class IndexView6(generic.ListView):
    template_name = 'what2drink/triplesec.html'
    context_object_name = 'triplesec_cocktails'

    def get_queryset(self):
        if Cocktail.objects.all().filter(spirit1__startswith='Tr'):
            return Cocktail.objects.all().filter(spirit1__startswith='Tr')
        if Cocktail.objects.all().filter(spirit2__startswith='Tr'):
            return Cocktail.objects.all().filter(spirit2__startswith='Tr')
        if Cocktail.objects.all().filter(spirit3__startswith='Tr'):
            return Cocktail.objects.all().filter(spirit3__startswith='Tr')
        if Cocktail.objects.all().filter(spirit4__startswith='V'):
            return Cocktail.objects.all().filter(spirit4__startswith='Tr')
        if Cocktail.objects.all().filter(spirit5__startswith='Tr'):
            return Cocktail.objects.all().filter(spirit5__startswith='Tr')



