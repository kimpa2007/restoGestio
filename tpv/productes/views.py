# -*- encoding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from models import Categoria, Producte, Opcio
from productes.forms import formProducte, formCategoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json

@login_required
def llistarProductes(request):
    if request.GET.has_key('categoria'):
        x = request.GET['categoria'] 
        c = Categoria.objects.filter(categoria = x)
        productes = Producte.objects.filter(categoria = c) 
        productesJson = serializers.serialize('json', productes)
        return HttpResponse(productesJson, content_type="application/json")    
    else:
        return render(request,'error.html')

@login_required
def llistarCategories(request):
    categories = Categoria.objects.all()
    paginator = Paginator(categories, 10) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(1)
    context = { 'categories' : categories }
    return render(request, 'llistaCategories.html', context)

@login_required
def llistarCategoriesAjax(request):
    categories = Categoria.objects.all()
    categoriesJson = serializers.serialize('json', categories)
    print categoriesJson
    return HttpResponse(categoriesJson, content_type="application/json")    

@login_required
def afegirProducte(request,categoria=None):
    if request.method == 'POST':
        form = formProducte(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producte afegit.')
            return HttpResponseRedirect(reverse('productes:llistarCategories'))
        else:
            messages.error(request, 'Error al afegir el producte')
            return render(request,'error.html')

    else:
        form = formProducte()
    camps_bootstrap = ('categoria','producte','preu','imatge')
    for c in camps_bootstrap:
        form.fields[c].widget.attrs['class'] = 'form-control'
    return render(request,'afegirProducte.html', {'form':form,})

@login_required
def afegirCategoria(request):
    if request.method == 'POST':
        form = formCategoria(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoria afegida')
            return HttpResponseRedirect(reverse('productes:llistarCategories'))
        else:
            messages.error(request, 'Error al afegir la categoria')
            return render(request,'error.html')

    else:
        form = formCategoria()
    form.fields['categoria'].widget.attrs['class'] = 'form-control'
    return render(request,'afegirCategoria.html', {'form':form})

@login_required
def editarProducte(request, idProducte):

    if idProducte is not None:
        producteExist = Producte.objects.filter(pk = idProducte).exists()
        if producteExist:
            producte = get_object_or_404(Producte, pk=idProducte)
            print producte
        else:
            messages.error(request, 'El producte a editar no existeix')
            return render(request,'error.html')

    if request.method == 'POST':
        form = formProducte(request.POST, request.FILES, instance = producte)
        if form.is_valid():
            messages.success(request, 'Producte editat')
        else:
            messages.error(request, 'Error editant el producte')
            return render(request,'error.html')

    else:
        form = formProducte(instance=producte)
    return render(request, 'editarProducte.html', {'form':form})

@login_required
def dadesProducte(request, idProducte):
     producteExist = Producte.objects.filter(pk = idProducte).exists()
     if producteExist:
         categoria = Producte.objects.filter(pk = idProducte).values('categoria')
         opcionsValides = Categoria.objects.filter(pk = categoria).values('opcio')
         res = []
         for o in opcionsValides:
             resposta = {}
             opcio = Opcio.objects.filter(pk = o['opcio'])
             for n in opcio:
                 print n
                 resposta['opcio'] = str(n)
             res.append(resposta)
         print res
     else:
         messages.error(request, 'Error amb el producte demanat')
         return render(request,'error.html')
     return HttpResponse(json.dumps(res), content_type="application/json")    
 
@login_required
def crearLinia(request, producte, opcio, comentari): 
        return render(request,'error.html')