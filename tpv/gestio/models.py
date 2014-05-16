from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	categoria = models.CharField(max_length=255)

class Producte(models.Model):
	categoria = models.ForeignKey(Categoria)
	producte = models.CharField(max_length=255)
	preu =  models.FloatField()

class Comanda(models.Model):
	usuari = models.ForeignKey(User)
	client = models.CharField(max_length=255)
	dataHora = models.DateTimeField(auto_now_add=True)
	metodePagament = models.CharField(max_length=255)
	total = models.FloatField()
	##metode per calcular?

class LiniaComanda(models.Model):
	comanda = models.ForeignKey(Comanda)
	producte = models.ForeignKey(Producte)
	quantitat = models.IntegerField()
	total = models.FloatField()
	##calcular auto total?(projecte)

