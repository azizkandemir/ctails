from django.db import models
from django.urls import reverse


class Cocktail(models.Model):
    taste = models.CharField(max_length=20)
    cocktail_name = models.CharField(max_length=50, primary_key='true')
    difficulty = models.CharField(max_length=20)
    cocktail_pic = models.CharField(max_length=1000)
    strength = models.CharField(max_length=20)
    #is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('cocktails:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.cocktail_name + ' - ' + self.taste



class Spirit(models.Model):
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    spirit_name = models.CharField(max_length=20)
    spirit_color = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.spirit_name
