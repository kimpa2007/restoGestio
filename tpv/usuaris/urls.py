# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from usuaris import views

urlpatterns = patterns('',
    url(r'^$', views.autenticacio, name='autenticacio'),
    url(r'^logout/$', views.desautenticacio, name='desautenticacio'), 
    url(r'^canviContrasenya/$', views.canviContrasenya, name='canviContrasenya'),     
)
