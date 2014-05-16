# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from gestio import views

urlpatterns = patterns('',
    url(r'^$', views.autenticacio, name='autenticacio'),
    url(r'^menu/$', views.menu, name='menu'),
    url(r'^logout/$', views.desautenticacio, name='desautenticacio'),
    url(r'^llistarProductes/$', views.llistarProductes, name='llistarProductes'),
    url(r'^llistarCategories/$', views.llistarCategories, name='llistarCategories'), 
    url(r'^canviContrasenya/$', views.canviContrasenya, name='canviContrasenya'),     
    ##Falta lo de editar i companyia
)
