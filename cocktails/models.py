from django.db import models


class Cocktail(models.Model):
    taste = models.CharField(max_length=250)
    cocktail_name = models.CharField(max_length=250, primary_key='true')
    difficulty = models.CharField(max_length=250)
    cocktail_pic = models.CharField(max_length=1000)

    def __str__(self):
        return self.cocktail_name + ' - ' + self.taste


class Spirits(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    spirit_name = models.CharField(max_length=50)
    spirit_color = models.CharField(max_length=50)
