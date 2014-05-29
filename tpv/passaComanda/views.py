# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from productes.models import Categoria
from comanda.models import Comanda, LiniaComanda
from usuaris.models import Usuari
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
def passaComanda(request):
    #Recuperar el nom del usuari
    usuari = request.user.id;
    comandeta = json.loads(request.GET.get('comandeta'))
    linies = comandeta['linies']
    taula = comandeta['taula']
    
    u = User.objects.get(id=usuari)
    t = Taula.objects.get(id=taula)
    c = Comanda()   

    c.usuari__id = u.id
    c.taula__id = t.id
    print "ua"
    print "no vull guardar res"
    
    for l in linies:
        quantitat = l['quantitat']
        comentari = l['comentari']
        producte = l['producte']
        moment = l['momentApat']
        opcio = l['opcio']
        
        li = LiniaComanda()
        li.comanda = c
        li.producte = producte
        li.total = quantitat
        li.commentari = comentari
        li.opcio = opcio
        li.momentApat = moment
        li.save()
    #Recuperar les dades de la comanda i crear la nova comanda
     #   request.POST.get('rrr')
    #Recuperar les linies i crear-les
    
      #  return HttpResponse(json.dumps(res), content_type="application/json")    
    return render(request,'error.html')  

