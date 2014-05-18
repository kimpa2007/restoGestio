from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from models import Categoria, Producte
from django.contrib.auth.decorators import login_required


@login_required
def llistarProductes(request):
    if request.GET.has_key('categoria'):
        x = request.GET['categoria'] 
        c = Categoria.objects.filter(categoria = x)
        productes = Producte.objects.filter(categoria = c) 
        productesJson = serializers.serialize('json', productes)
        return HttpResponse(productesJson, mimetype="application/json")    
    else:
        return render(request,'error.html')

@login_required
def llistarCategories(request):
    categories = Categoria.objects.all()
    context = { 'categories' : categories }
    return render(request, 'llistaCategories.html', context)