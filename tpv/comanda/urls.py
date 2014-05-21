# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from comanda import views

urlpatterns = patterns('',
    url(r'^$', views.llistarComandes, name='llistarComandes'),
    url(r'^llistarPendents/$', views.llistarComandesPendents, name='llistarComandesPendents'),
    url(r'^llistarTancades/$', views.llistarComandesTancades, name='llistarComandesTancades'),
    url(r'^veureDetalls/(?P<idComanda>\d+)$', views.veureDetalls, name='veureDetalls'),
    url(r'^tancarComanda/(?P<idComanda>\d+)/$', views.tancarComanda, name='tancarComanda'),

)
