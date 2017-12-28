from django.db import models
from django.urls import reverse


class UserCocktail(models.Model):
    taste = models.CharField(max_length=20)
    cocktail_name = models.CharField(max_length=50, primary_key='true')
    difficulty = models.CharField(max_length=20)
    cocktail_pic = models.FileField()
    strength = models.CharField(max_length=20)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('usercocktails:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.cocktail_name + ' - ' + self.taste
