# -*- coding: utf8 -*-
from gestio.models import Categoria, Usuari

def crea():
    
    usuari = Usuari()
    usuari.password("ies")
    usuari.username("claude")
    usuari.first_name("Claude")
    usuari.last_name("Chaillet")
    usuari.is_staff(1)
    usuari.is_active(1)