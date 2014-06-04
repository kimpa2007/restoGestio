# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
import datetime
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import formats
from django.shortcuts import render, get_object_or_404
from comanda.models import Comanda, LiniaComanda, MomentApat, Taula
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json 
from django.http import StreamingHttpResponse
from usuaris.models import Usuari
from productes.models import Producte, Opcio, Categoria
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

@login_required
def menu(request):
    dh = datetime.datetime.now()
    dataHora1 = formats.date_format(dh, 'DATETIME_FORMAT')
    context = {}
    context['data'] = dataHora1
    return render(request, 'menu.html',context)

def dataHora(request):
    dh = datetime.datetime.now()
    dataHora1 = formats.date_format(dh, 'DATETIME_FORMAT')
    dataHora = json.dumps(dataHora1, cls=DjangoJSONEncoder)
    return HttpResponse(dataHora, content_type="application/json")  


# Create your views here.
@login_required
def llistarComandes(request):
    comandes = Comanda.objects.all()
    paginator = Paginator(comandes, 20) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        comandes = paginator.page(page)
    except PageNotAnInteger:
        comandes = paginator.page(1)
    except EmptyPage:
        comandes = paginator.page(1)    
    context = { 'comandes' : comandes }
    return render(request, 'llistaComandes.html', context)

@login_required
def llistarComandesPendents(request):
    comandesPendents = Comanda.objects.filter(estat='Pendent');
    paginator = Paginator(comandesPendents, 20) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        comandesPendents = paginator.page(page)
    except PageNotAnInteger:
        comandesPendents = paginator.page(1)
    except EmptyPage:
        comandesPendents = paginator.page(1)      
    
    context = { 'comandesPendents' : comandesPendents }
    return render(request, 'comandesPendents.html', context)


@login_required
def llistarComandesTancades(request):
    comandes = Comanda.objects.filter(estat='Tancada');
    paginator = Paginator(comandes, 20) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        comandes = paginator.page(page)
    except PageNotAnInteger:
        comandes = paginator.page(1)
    except EmptyPage:
        comandes = paginator.page(1)      
    context = { 'comandes' : comandes }
    return render(request, 'comandesTancades.html', context)

@login_required
def llistarComandesPagades(request):
    comandes = Comanda.objects.filter(Q(estat='Pagada') | Q(estat='pagada'));
    paginator = Paginator(comandes, 20) #Quantes solicituds volem mostrar
    page = request.GET.get('pagina') #('pagina') és el que s'assignara al get
    try:
        comandes = paginator.page(page)
    except PageNotAnInteger:
        comandes = paginator.page(1)
    except EmptyPage:
        comandes = paginator.page(1)      
    
    
    context = { 'comandes' : comandes }
    print comandes
    return render(request, 'comandesPagades.html', context)

@login_required
def veureDetalls(request, idComanda):
    comandaExist = Comanda.objects.filter(pk = idComanda).exists()
    if comandaExist:
        comanda = get_object_or_404(Comanda, pk=idComanda)
        liniesComandes = LiniaComanda.objects.filter(comanda=idComanda).order_by('momentApat')
        context = { 'comanda' : comanda , 'liniesComandes': liniesComandes }
    else:
        messages.error(request, 'No es poden veure els detalls d\'una comanda que no existeix.')
        return render(request,'error.html')
    return render(request, 'veureDetalls.html', context)

@login_required
def tancarComanda(request, idComanda):
    comandaExist = Comanda.objects.filter(pk = idComanda).exists()
    if comandaExist:
        if comandeta.estat != 'tancada':
            comandeta.estat = 'Tancada';
            comandeta.save()
            messages.success(request, 'Comanda tancada')
            return HttpResponseRedirect(reverse('gestio:llistarComandesPendents'))
    else:
        messages.error(request, 'No es poden tancar una comanda que no existeix.')
        return render(request,'error.html')
    return HttpResponseRedirect(reverse('gestio:llistarComandesPendents'))

def pagarComanda(request, idComanda):
    comandaExist = Comanda.objects.filter(pk = idComanda).exists()
    if comandaExist:
        comandeta = Comanda.objects.get(pk=idComanda)
        if comandeta.estat != 'tancada':
            comandeta.estat = 'Tancada';
            comandeta.save()
            messages.success(request, 'Comanda tancada')
            return HttpResponseRedirect(reverse('comandes:llistarComandesPendents'))
    else:
        messages.error(request, 'No es poden tancar una comanda que no existeix.')
        return render(request,'error.html')
    return HttpResponseRedirect(reverse('gestio:llistarComandesTancades'))

def guardarPagament(request, idComanda, pagament):
    comandaExist = Comanda.objects.filter(pk = idComanda).exists()
    if comandaExist:
        r = {"ok": "ok"}
        resposta= json.dumps(r)
        c = Comanda.objects.get(pk=idComanda)
        c.metodePagament = pagament;
        c.estat = "Pagada";
        c.save()
    else:
        messages.error(request, 'No es pot tancar una comanda que no existeix.')
        return render(request,'error.html')
    return StreamingHttpResponse(resposta, content_type="application/json") 

def donaCanvi(request, qtatDonada, total):
   
    torna = round(float(qtatDonada) - float(total),2);

    if torna <0:
        n = {"res": "Falta"}
    else:
        n = {"res": torna}
    resposta = json.dumps(n)
    
    return StreamingHttpResponse(resposta, content_type="application/json") 
