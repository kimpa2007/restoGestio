# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator

metode_pagament_choice = (('targeta','Targeta'),('effectiu','Effectiu')	)
estat_comanda_choice = (('pendent','Pendent'),('tancada','Tancada'),('curs','En curs'))
roles_choice = (('usuari','Usuari Pelat'),('adminSis','Administrador de l\'aplicació'))

class MomentApat(models.Model):
	descripcio = models.CharField(max_length=255)

class Categoria(models.Model):
	categoria = models.CharField(max_length=255)

class Opcio(models.Model):
	descripcio = models.TextField(max_length=255)
	
class Producte(models.Model):
	categoria = models.ForeignKey(Categoria)
	producte = models.CharField(max_length=255)
	preu =  models.DecimalField(max_digit=4,decimal_places=2,default=0)
	imatge = models.ImageField(upload_to="productes", null=True, blank=True)
	commentari = models.TextField(validators=[MaxLengthValidator(200)])
	opcio = models.ManyToManyField(Opcio)
	
class Taula(models.Model):
	capacitat = models.IntegerField()

class Usuari(User):
	esAdminSistema = models.CharField(max_length=255, choices=roles_choice) 

class Comanda(models.Model):
	usuari = models.ForeignKey(Usuari)
	taula = models.ForeignKey(Taula)
	dataHora = models.DateTimeField(auto_now_add=True)
	metodePagament = models.CharField(max_length=255, choices=metode_pagament_choice)
	estat = models.CharField(max_length=255, choices=estat_comanda_choice) 
	total = models.FloatField()
	##metode per calcular?

class LiniaComanda(models.Model):
	comanda = models.ForeignKey(Comanda)
	producte = models.ForeignKey(Producte)
	quantitat = models.IntegerField()
	total = models.FloatField()
	##calcular auto total?(projecte)

