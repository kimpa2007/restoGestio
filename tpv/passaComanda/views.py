# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from productes.models import Categoria
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
        print taulesJson
    return StreamingHttpResponse(taulesJson, content_type="application/json")    
