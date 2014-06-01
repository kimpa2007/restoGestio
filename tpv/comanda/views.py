# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404
from comanda.models import Comanda, LiniaComanda, MomentApat, Taula
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json 
from django.http import StreamingHttpResponse
from productes.models import Categoria
from usuaris.models import Usuari
from productes.models import Producte, Opcio
from django.contrib.auth.models import User
from django.core import serializers
from comanda.models import Taula
from django.db.models import Q

# Create your views here.
@login_required
def llistarComandes(request):
    comandes = Comanda.objects.all()
    context = { 'comandes' : comandes }
    return render(request, 'llistaComandes.html', context)

@login_required
def llistarComandesPendents(request):
    comandesPendents = Comanda.objects.filter(estat='Pendent');
    context = { 'comandesPendents' : comandesPendents }
    return render(request, 'comandesPendents.html', context)


@login_required
def llistarComandesTancades(request):
    comandes = Comanda.objects.filter(estat='Tancada');
    context = { 'comandes' : comandes }
    return render(request, 'comandesTancades.html', context)

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
        comandeta = Comanda.objects.get(pk=idComanda)
        if comandeta.estat != 'tancada':
            comandeta.estat = 'Tancada';
            comandeta.save()
            messages.success(request, 'Comanda tancada')
            return HttpResponseRedirect(reverse('comandes:llistarComandesPendents'))
    else:
        messages.error(request, 'No es poden tancar una comanda que no existeix.')
        return render(request,'error.html')
    return HttpResponseRedirect(reverse('comandes:llistarComandesPendents'))

@login_required
def recuperarMomentsApat(request):
     if(request.method == "GET"):
         momentsAp = MomentApat.objects.all().exists()
         res = []
         if momentsAp:
             opcio = MomentApat.objects.values('descripcio')
             for n in opcio:
                    resposta = {}
                    resposta['moment'] = n             
                    res.append(resposta)
         else:
             resposta = {}
             resposta['error'] = "Error amb els moments apats."
         return HttpResponse(json.dumps(res), content_type="application/json")  
     else:
         return render(request,'error.html')  
     
@login_required
def recuperarLinies(request, idComanda):
    comandaExist = Comanda.objects.filter(pk = idComanda).exists()
    if comandaExist:
        c = Comanda.objects.get(pk = idComanda)
        if c.estat == 'tancada':
            messages.error(request, 'Aquesta comanda està tancada')
            return render(request, 'error.html')
        else:
            ##Falta recuperar el valor real de producte, opcio o momentapat
            linies = LiniaComanda.objects.filter(comanda = c)
            res = []
            for l in linies:
                resposta = {}
                resposta['id'] = str(l.id)
                resposta ['producte'] = str(l.producte)
                resposta['opcio'] =  str(l.opcio)
                resposta['total'] = str(l.total)
                resposta['momentApat'] = str(l.momentApat.descripcio)
                res.append(resposta)
            return StreamingHttpResponse(json.dumps(res), content_type="application/json")    
    else:
        messages.error(request, 'No existeix aquesta comanda')
        return render(request, 'error.html')
    
@login_required
def recuperaIdComanda(request,idTaula):
    if idTaula is not None:
        t = Taula.objects.filter(pk = idTaula).exists()
        if t:
            comandes = Comanda.objects.filter(taula = idTaula)
            for c in comandes:
                if c.estat == 'Pendent' or c.estat == 'pendent':
                    n = {'idComanda': c.id}
                    idComanda = json.dumps(n)
                    return StreamingHttpResponse(idComanda, content_type="application/json")    

    n = {'idComanda': 'error'}
    idComanda = json.dumps(n)
    return StreamingHttpResponse(idComanda, content_type="application/json")    

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
 
@login_required
def editaComanda(request):
    comandeta = json.loads(request.GET.get('comandeta'))
    taula = Taula.objects.get(id=comandeta['taula'])
    idComanda = comandeta['id']
    Comanda.objects.filter(pk = id).update(usuari = request.user)

    #Recuperar les linies i crear-les
    for l in linies:
        quantitat = l['quantitat']
        comentari = l['comentari'] 
        producte = Producte.objects.get(producte= l['producte'])

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
