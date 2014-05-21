# -*- encoding: utf-8 -*-

from django import  forms
from productes.models import Producte, Categoria
from django.forms import ModelForm

class formProducte(ModelForm):
    class Meta:
        model = Producte
    producte = forms.CharField(max_length=255, label="Nom del Producte")
    preu = forms.DecimalField()
    imatge = forms.ImageField(required=False)
    
class formCategoria(ModelForm):
    class Meta:
        model = Categoria
    categoria = forms.CharField(required=True, max_length=255, label="Nom de la categoria")