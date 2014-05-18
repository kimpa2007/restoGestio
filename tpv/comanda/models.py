# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from usuaris.models import Usuari
from productes.models import Producte, Opcio
metode_pagament_choice = (('targeta','Targeta'),('effectiu','Effectiu')    )
estat_comanda_choice = (('pendent','Pendent'),('tancada','Tancada'),('curs','En curs'))
moment_apat_choice = (('apertiu','Aperitiu'),('entrant','Entrant'),('segonplat','Segon plat'),('postre','Postre'))

    

class Taula(models.Model):
    capacitat = models.IntegerField()
    def __unicode__(self):
        return '%i %i' % (self.id, self.capacitat)

class Comanda(models.Model):
    usuari = models.ForeignKey(Usuari)
    taula = models.ForeignKey(Taula)
    dataHora = models.DateTimeField(auto_now_add=True)
    metodePagament = models.CharField(max_length=255, choices=metode_pagament_choice)
    estat = models.CharField(max_length=255, choices=estat_comanda_choice) 
    total = models.FloatField()
    def __unicode__(self):
        return self.id
    ##metode per calcular?

##Ja que poden haber-hi cocions i acompanyament diferents no es pot posar el camp de quantitat
class LiniaComanda(models.Model):
    comanda = models.ForeignKey(Comanda)
    producte = models.ForeignKey(Producte)
    total = models.FloatField()
    commentari = models.TextField(validators=[MaxLengthValidator(200)])
    opcio = models.ManyToManyField(Opcio)
    momentApat = models.CharField(max_length=255, choices=moment_apat_choice)
    ##calcular auto total?(projecte)
    def __unicode__(self):
        return self.comanda

