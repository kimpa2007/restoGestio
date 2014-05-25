# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from usuaris.models import Usuari
from productes.models import Producte

metode_pagament_choice = (('targeta','Targeta'),('effectiu','Effectiu')    )
estat_comanda_choice = (('pendent','Pendent'),('tancada','Tancada'),('curs','En curs'))
moment_apat_choice = (('apertiu','Aperitiu'),('entrant','Entrant'),('segon','Segon plat'),('postre','Postre'))
taula_choice = (('ocupada','ocupada'),('disponible','disponible'))
    

class Taula(models.Model):
    capacitat = models.IntegerField()
    estat = models.CharField(max_length=255, choices=taula_choice, default='disponible')

class Comanda(models.Model):
    usuari = models.ForeignKey(Usuari)
    taula = models.ForeignKey(Taula)
    dataHora = models.DateTimeField(auto_now_add=True)
    metodePagament = models.CharField(max_length=255, choices=metode_pagament_choice, null=True, blank=True)
    estat = models.CharField(max_length=255, choices=estat_comanda_choice) 
    total = models.FloatField(null=True, blank=True)
    
    def clean(self):
        #comprovar que la taul està lliure
        #self.taula.estat = 'ocupada'
        pass 

    
##Ja que poden haber-hi cocions i acompanyament diferents no es pot posar el camp de quantitat
class LiniaComanda(models.Model):
    comanda = models.ForeignKey(Comanda)
    producte = models.ForeignKey(Producte)
    total = models.FloatField(null=True, blank=True)
    commentari = models.TextField(validators=[MaxLengthValidator(200)], null=True, blank=True)
    ##opcio = models.ManyToManyField(Opcio, null=True, blank=True)
    momentApat = models.CharField(max_length=255, choices=moment_apat_choice)
    ##calcular auto total?(projecte)


def post_save_comanda(sender, instance, created, **kwargs):
    if created:
        instance.taula.estat = 'ocupada'
        instance.taula.save()
    
from django.db.models.signals import post_save
post_save.connect(post_save_comanda, sender=Comanda)

    
    
