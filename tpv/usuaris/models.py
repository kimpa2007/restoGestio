# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

roles_choice = (('usuari','Usuari Pelat'),('adminSis','Administrador de l\'aplicació'),('cuina','cuina'),('cambrer','cambrer'))

class Usuari(User):
    esAdminSistema = models.CharField(max_length=255, choices=roles_choice) 
    usuari = models.OneToOneField(User)
    def __unicode__(self):
        return self.username