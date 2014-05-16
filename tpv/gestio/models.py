from django.db import models
from django.contrib.auth.models import User

metode_pagament_choice = (('targeta','Targeta'),('effectiu','Effectiu')	)
estat_comanda_choice = (('pendent','Pendent'),('tancada','Tancada'),('curs','En curs'))

class Categoria(models.Model):
	categoria = models.CharField(max_length=255)

class Producte(models.Model):
	categoria = models.ForeignKey(Categoria)
	producte = models.CharField(max_length=255)
	preu =  models.FloatField()
	imatge = models.FileField(upload_to="productes", blank=True)

class Comanda(models.Model):
	usuari = models.ForeignKey(User)
	client = models.CharField(max_length=255)
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

