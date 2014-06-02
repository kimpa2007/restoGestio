# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.autenticacio, name='autenticacio'),
    url(r'^logout/$', views.desautenticacio, name='desautenticacio'), 
    url(r'^dadesUsuari/$', views.dadesUsuari, name='dadesUsuari'),
    url(r'^extreureDades/$', views.extreureDades, name='extreureDades'),     
    url(r'^canviContrasenya/$', views.canviContrasenya, name='canviContrasenya'),     
)
