from django.http import HttpResponse
from .models import Cocktail
from django.template import loader


def index(request):
    all_cocktails = Cocktail.objects.all()
    template = loader.get_template('cocktails/index.html')
    context = {
        'all_cocktails': all_cocktails,
    }
    """
    html = ''
    for cocktail in all_cocktails:
        url = '/cocktails/' + str(cocktail.id) + '/'
        html += '<a href="' + url + '">' + cocktail.cocktail_name + '</a><br>'"""
    return HttpResponse(template.render(context, request))


def detail(request, cocktail_name):
    return HttpResponse("<h2>Details for cocktail name: " + str(cocktail_name) + "</h2>")