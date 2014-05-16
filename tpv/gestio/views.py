# -*- encoding: utf-8 -*-
from django.shortcuts import render
from gestio.forms import formulariLogin, formulariCanvi
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset
from gestio.models import Categoria
import re
import hashlib

# Funció per autenticar usuaris
def autenticacio(request):
#Si POST hi han dades  per processar
    if request.method == 'POST': 
        form = formulariLogin(request.POST)
        if request.user.is_authenticated():
            defaultNext = reverse('gestio:menu')
            next = request.GET.get('next',defaultNext)
            return HttpResponseRedirect(next)
        #Comprovar si les dades entrades són correctes 
        if form.is_valid():
            #Emmagatzemem les dades que es troben al diccioanri form.cleaned_data a les variables corresponents
            username = form.cleaned_data['usuari']
            password = form.cleaned_data['contrasenya']
            #Autenticar usuaris
            user = authenticate(username=username, password=password)
            #Si les dades són correctes i si l'usuari es correcte s'envia a la pàgina demanada.
            #Es comprova totes les dades juntes per no donar massa informació sobre el perquè falla la identificació.
            if user is not None:
                if user.is_active:
                    login(request, user)
                    defaultNext = reverse('gestio:menu')
                    ##Variable defaultnext per evitar hardcored i problemes per si internacionalització
                    next = request.GET.get('next',defaultNext)
                    return HttpResponseRedirect(next)
                else:
                    ## Enviar cap a un formulari de reset.
                    ## Muntar un servidor de correu i fer-ho en local
                    messages.error(request, "Compta desactivada")
                    return render(request, 'error.html')
            else:
                messages.error(request, 'Credencials incorrectes')
                return render(request, 'error.html')
            
        else:
            messages.error(request, 'Ep! Hi ha hagut un error!')
            return render(request, 'error.html')
        #Si no es pots es GET i vol dir que no tenim dades a processar per l'ho tant pintem el formulari
    else:
        form = formulariLogin() 
    
    camps_bootstrap = ('usuari', 'contrasenya')
    for c in camps_bootstrap:
        form.fields[c].widget.attrs['class'] = 'form-control'
    #Per defecte enviem el formulari.     
    return render(request, 'login.html', {  'form': form })


#Desautenticar un usuari
@login_required
def desautenticacio(request):
    logout(request)
    messages.success(request, 'Logout correcte, a reveure')
    return HttpResponseRedirect('/gestio')
    

@login_required
def menu(request):
    return render(request, 'menu.html')


def llistarProductes(request):
    return HttpResponseRedirect(request, 'llistaProductes.html')

def llistarCategories(request):
    categories = Categoria.objects.all()
    context = { 'categories' : categories }
    return render(request, 'llistaCategories.html', context)


def canviContrasenya(request):
    if request.method == 'POST': 
        form = formulariCanvi(request.POST)
        if form.is_valid():
            novaContrasenya1 = form.cleaned_data['novaContrasenya1']
            novaContrasenya2 = form.cleaned_data['novaContrasenya2']
            
            #Comprovar que les contrasenyes no siguin massa senzilles
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', novaContrasenya1):
                if novaContrasenya1 != novaContrasenya2:
                    messages.error(request, "Les noves contrasenyes no es correponen.")
                    return render(request, 'error.html')
                else:
                    usuari.set_password(novaContrasenya1)
                    usuari.save()
                    messages.success(request, "Contrasenya cambiada")
            else:
                messages.error(request, "Contrasenya massa senzilla.")
    else:
        form = formulariCanvi() 

    return render(request, 'canviPassword.html', {  'form': form })