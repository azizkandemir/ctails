from .models import Cocktail, Spirit, UserCocktail
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth import *

class IndexView(generic.ListView):
    template_name = 'cocktails/index.html'
    context_object_name = 'all_cocktails'

    def get_queryset(self):
        return Cocktail.objects.all()

class DetailView(generic.DetailView):
    model = Cocktail
    template_name = 'cocktails/detail.html'
    context_object_name = 'all_cocktails'

class CocktailCreate(CreateView):
    model = Cocktail
    fields = ['taste', 'cocktail_name', 'difficulty', 'strength', 'cocktail_pic']

class CocktailUpdate(UpdateView):
    model = Cocktail
    fields = ['taste', 'cocktail_name', 'difficulty', 'strength', 'cocktail_pic']

class CocktailDelete(DeleteView):
    model = Cocktail
    success_url = reverse_lazy('cocktails:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'cocktails/registration_form.html'

    # displays blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)

            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('cocktails:index')

        return render(request, self.template_name, {'form': form})


def favorite_cocktail(request, cocktail_name):
    cocktail = get_object_or_404(Cocktail, pk=cocktail_name)
    try:
        if cocktail.is_favorite:
            cocktail.is_favorite = False
        else:
            cocktail.is_favorite = True
        cocktail.save()
    except (KeyError, Cocktail.DoesNotExist):
        return JsonResponse({'success': False})

    else:
        return JsonResponse({'success': True})

#def index(request):
    #all_cocktails = Cocktail.objects.all()
    #context = {'all_cocktails': all_cocktails}
    #"""
    #html = ''
    #for cocktail in all_cocktails:
    #    url = '/cocktails/' + str(cocktail.id) + '/'
    #    html += '<a href="' + url + '">' + cocktail.cocktail_name + '</a><br>'"""
    #return render(request, 'cocktails/index.html', context)


#def detail(request, cocktail_name):
    #"""try:
    #    ctail = Cocktail.objects.get(pk=cocktail_name)
    #except Cocktail.DoesNotExist:
    #    raise Http404("Cocktail does not exist")"""
    #ctail = get_object_or_404(Cocktail, pk=cocktail_name)
    #return render(request, 'cocktails/detail.html', {'ctail': ctail})

"""def favorite(request, cocktail_name):

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
        return render(request, 'cocktails/detail.html', {'ctail': ctail})"""

