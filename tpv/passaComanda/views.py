# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from productes.models import Categoria
from comanda.models import Comanda, LiniaComanda, MomentApat
from usuaris.models import Usuari
from productes.models import Producte, Opcio
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core import serializers
from comanda.models import Taula
from django.http import StreamingHttpResponse
from django.db.models import Q
import json

@login_required
def pintatpv(request):
    return render(request, 'pintaTpv.html')

@login_required
def donaTaules(request):
    #Només es pot crear una comanda nova a una taula que no estigui ocupada!
    taules = Taula.objects.filter(estat = 'disponible').exists()
    if taules:
        taules = Taula.objects.filter(estat = 'disponible')
        taulesJson = serializers.serialize('json', taules)
    else:
        n = {'pk': "error"}
        taulesJson = json.dumps(n)
    return StreamingHttpResponse(taulesJson, content_type="application/json")    

@login_required
def taulesOccupades(request):
    #Només es pot crear una comanda nova a una taula que no estigui ocupada!
    taules = Taula.objects.filter(estat = 'ocupada').exists()
    if taules:
        taules = Taula.objects.filter(estat = 'ocupada')
        taulesJson = serializers.serialize('json', taules)
    else:
        n = {'pk': "error"}
        taulesJson = json.dumps(n)
    return StreamingHttpResponse(taulesJson, content_type="application/json")    

@login_required
def passaComanda(request):
    #Recuperar les dades json
    
    comandeta = json.loads(request.GET.get('comandeta'))
    taula = Taula.objects.get(id=comandeta['taula'])
    #Recuperar les dades de la comanda i crear la nova comanda

    c = Comanda()   
    c.usuari = request.user
    linies = comandeta['linies']
    c.taula = taula    
    c.estat = 'Pendent'
    c.save()
    
    #Recuperar les linies i crear-les
    for l in linies:
        quantitat = l['quantitat']
        comentari = l['comentari'] 
        producte = Producte.objects.get(producte= l['producte'])
        print comandeta.has_key('opcio')

        if comandeta.has_key('opcio'):
            opcio = Opcio.objects.get(opcio = l['opcio'] )
            li.opcio = opcio

        moment = MomentApat.objects.get(descripcio = l['momentApat'])
        
        li = LiniaComanda()
        li.comanda = c
        li.producte = producte
        li.total = quantitat
        li.commentari = comentari
        li.momentApat = moment
        li.save()
        
    n = {'res': "ok"}
    resposta = json.dumps(n)
    return StreamingHttpResponse(resposta, content_type="application/json")    

