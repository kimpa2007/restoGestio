from django.shortcuts import render, get_object_or_404
from models import Comanda, LiniaComanda, MomentApat
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
import json 
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
        print comandeta.estat
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
             print opcio
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
 