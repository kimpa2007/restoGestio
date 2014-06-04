# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from comanda import views

urlpatterns = patterns('',
    url(r'^$', views.pintatpv, name='pintatpv'),
    url(r'^momentApat/$', views.recuperarMomentsApat, name='recuperarMomentsApat'),
    url(r'^recuperarLinies/(?P<idComanda>\d+)/$', views.recuperarLinies, name='recuperarLinies'),
    url(r'^donaTaules/$', views.donaTaules, name='donaTaules'),
    url(r'^taulesOccupades/$', views.taulesOccupades, name="taulesOccupades"),
    url(r'^passaComanda/$', views.passaComanda, name='passaComanda'),
    url(r'^recuperaIdComanda/(?P<idTaula>\d+)/$', views.recuperaIdComanda, name='recuperaIdComanda'),
    url(r'^editaComanda/$', views.editaComanda, name='editaComanda'),
    url(r'^obtenirTotal/(?P<idComanda>\d+)/$', views.obtenirTotal, name='obtenirTotal'),

)
