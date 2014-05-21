from django.shortcuts import render, get_object_or_404
from models import Comanda, LiniaComanda
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
@login_required
def llistarComandes(request):
    comandes = Comanda.objects.all()
    context = { 'comandes' : comandes }
    return render(request, 'llistaComandes.html', context)

@login_required
def llistarComandesPendents(request):
    comandesPendents = Comanda.objects.filter(estat='Pendent');
    for c in comandesPendents:
        print c.id
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
