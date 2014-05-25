# -*- encoding: utf-8 -*-

from django.db import models

class Opcio(models.Model):
    descripcio = models.TextField(max_length=255)
    def __unicode__(self):
        return self.descripcio
    
class Categoria(models.Model):
    categoria = models.CharField(max_length=255)
    imatge = models.ImageField(upload_to="categories")
    opcio = models.ManyToManyField(Opcio, null=True, blank=True)
    def __unicode__(self):
        return self.categoria
    
class Producte(models.Model):
    categoria = models.ForeignKey(Categoria)
    producte = models.CharField(max_length=255)
    preu =  models.DecimalField(max_digits=4,decimal_places=2,default=0)
    imatge = models.ImageField(upload_to="productes", null=True, blank=True)
    def __unicode__(self):
        return self.producte
