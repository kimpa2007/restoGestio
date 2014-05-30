# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from comanda import views

urlpatterns = patterns('',
    url(r'^$', views.pintatpv, name='pintatpv'),
    url(r'^llistarComandes/$', views.llistarComandes, name='llistarComandes'),
    url(r'^llistarPendents/$', views.llistarComandesPendents, name='llistarComandesPendents'),
    url(r'^llistarTancades/$', views.llistarComandesTancades, name='llistarComandesTancades'),
    url(r'^veureDetalls/(?P<idComanda>\d+)$', views.veureDetalls, name='veureDetalls'),
    url(r'^tancarComanda/(?P<idComanda>\d+)/$', views.tancarComanda, name='tancarComanda'),
    url(r'^momentApat/$', views.recuperarMomentsApat, name='recuperarMomentsApat'),
    url(r'^recuperarLinies/(?P<idComanda>\d+)/$', views.recuperarLinies, name='recuperarLinies'),
    url(r'^donaTaules/$', views.donaTaules, name='donaTaules'),
    url(r'^taulesOccupades/$', views.taulesOccupades, name="taulesOccupades"),
    url(r'^passaComanda/$', views.passaComanda, name='passaComanda'),
    url(r'^recuperaIdComanda/(?P<idTaula>\d+)/$', views.recuperaIdComanda, name='recuperaIdComanda'),
)
