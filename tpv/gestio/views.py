# -*- encoding: utf-8 -*-
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

@login_required
def menu(request):
    return render(request, 'menu.html')


