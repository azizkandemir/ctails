from .models import Cocktail, Spirit
from django.shortcuts import render, get_object_or_404


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
    """try:
        ctail = Cocktail.objects.get(pk=cocktail_name)
    except Cocktail.DoesNotExist:
        raise Http404("Cocktail does not exist")"""
    ctail = get_object_or_404(Cocktail, pk=cocktail_name)
    return render(request, 'cocktails/detail.html', {'ctail': ctail})

def favorite(request, cocktail_name):

    ctail = get_object_or_404(Cocktail, pk=cocktail_name)
    try:
        selected_spirit = ctail.spirit_set.get(pk=request.POST['spirit'])
    except (KeyError, Spirit.DoesNotExist):
        return render(request, 'cocktails/detail.html', {
            'ctail': ctail,
            'error_message': "You did not select a valid spirit",
        })
    else:
        if selected_spirit.is_favorite:
            selected_spirit.is_favorite = False
            selected_spirit.save()
        else:
            selected_spirit.is_favorite = True
            selected_spirit.save()
        return render(request, 'cocktails/detail.html', {'ctail': ctail})
