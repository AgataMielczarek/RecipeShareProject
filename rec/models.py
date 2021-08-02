from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=250)
    time = models.CharField(max_length=8)
    servings = models.CharField(max_length=3)
    ingridients = models.TextField()
    desc = models.TextField()

    cuisines = [
        ('', 'Choose one'),
        ('tr', 'Traditional'),
        ('vt', 'Vegetarian'),
        ('ve', 'Vegan'),
    ]
    cuisine = models.CharField(max_length=2, choices=cuisines, default='')

    levels = [
        ('', 'Choose one'),
        ('e', 'Easy'),
        ('m', 'Medium'),
        ('h', 'Hard'),
    ]
    level = models.CharField(max_length=1, choices=levels, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # favourites
    # pictures
    # comments
    
    

    def __str__(self):
        return self.name


