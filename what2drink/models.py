from django.db import models
from cocktails.models import Cocktail, Spirit

"""class SelectedCocktails(models.Model):
    s_cocktail = ''
    s = Spirit.objects.all()
    a = ''
    b = ''
    c = ''
    d = ''
    e = ''
    spirit_dict = {
        "Vodka" : "S1", "Tequila" : "S2", "Gin" : "S3",
        "Rom" : "S4", "Triple Sec" : "S5"}
    for i in spirit_dict:
        if s.get(spirit_name__startswith="V") == i:
            a = i
            break
        elif s.get(spirit_name__startswith="T") == i:
            b = i
            break
        elif s.get(spirit_name__startswith="Gin") == i:
            c = i
            break
        elif s.get(spirit_name__startswith="R") == i:
            d = i
            break
        elif s.get(spirit_name__startswith="Tr") == i:
            e = i
            break
        else:
            print("There is no spirit right now...")
    all_cocktails = Cocktail.objects.all()
    q = ''
    w = ''
    o = ''
    f = ''
    g = ''
    for s in all_cocktails:
        if s.spirit1 == a:
            s = q
            break
        elif s.spirit2 == a:
            s = w
            break
        elif s.spirit3 == a:
            s = o
            break
        elif s.spirit4 == a:
            s = f
            break
        elif s.spirit5 == a:
            s = g
            break
        else:
            print("Nevermind")



    }"""

