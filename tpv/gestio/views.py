# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import datetime
from django.core import serializers
import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.utils import formats

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