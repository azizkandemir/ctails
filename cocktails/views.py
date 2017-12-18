from django.http import Http404
from .models import Cocktail
from django.shortcuts import render


def index(request):
    all_cocktails = Cocktail.objects.all()
    context = {'all_cocktails': all_cocktails}
    """
    html = ''
    for cocktail in all_cocktails:
        url = '/cocktails/' + str(cocktail.id) + '/'
        html += '<a href="' + url + '">' + cocktail.cocktail_name + '</a><br>'"""
    return render(request, 'cocktails/index.html', context)


def detail(request, cocktail_name):
    try:
        ctail = Cocktail.objects.get(pk=cocktail_name)
    except Cocktail.DoesNotExist:
        raise Http404("Cocktail does not exist")
    return render(request, 'cocktails/detail.html', {'ctail': ctail})
