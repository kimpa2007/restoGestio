# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

roles_choice = (('usuari','Usuari Pelat'),('adminSis','Administrador de l\'aplicació'),('cuina','cuina'),('cambrer','cambrer'))

class Usuari(models.Model):
    esAdminSistema = models.CharField(max_length=255, choices=roles_choice) 
    usuari = models.OneToOneField(User)
    def __unicode__(self):
        return self.usuari.username
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuari.objects.create(usuari=instance)
#Cada cop es faci un save a la taula Users, s'executa create_user_profile
post_save.connect(create_user_profile, sender=User)
