from django import forms
from .models import Recipe

class RecForm(forms.ModelForm):
    class Meta:
        model = Recipe
        exclude = ('user',)