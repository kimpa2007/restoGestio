# -*- encoding: utf-8 -*-

from django.shortcuts import render,get_object_or_404
from django.core import serializers
from django.http import HttpResponse
from models import Categoria, Producte
from productes.forms import formProducte, formCategoria
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
        
        
        
    if categoria is not None: 
        print "ok"
        #formulari am el cat selecionat
    else:
        print "no cat"
        #formilari am el cat sense selecionar
        
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
            messages.success(request, 'Categoria afegia')
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
        print producteExist
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
