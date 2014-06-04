# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from gestio import views

urlpatterns = patterns('',
    url(r'^$', views.menu, name='menu'),
    url(r'^dataHora/$', views.dataHora, name='dataHora'),
    url(r'^llistarComandes/$', views.llistarComandes, name='llistarComandes'),
    url(r'^llistarPendents/$', views.llistarComandesPendents, name='llistarComandesPendents'),
    url(r'^llistarTancades/$', views.llistarComandesTancades, name='llistarComandesTancades'),
    url(r'^llistarPagades/$', views.llistarComandesPagades, name='llistarComandesPagades'),
    url(r'^veureDetalls/(?P<idComanda>\d+)$', views.veureDetalls, name='veureDetalls'),
    url(r'^tancarComanda/(?P<idComanda>\d+)/$', views.tancarComanda, name='tancarComanda'),
    url(r'^guardarPagament/(?P<idComanda>\d+)/(?P<pagament>\w+)/$', views.guardarPagament, name='guardarPagament'),
    url(r'^donaCanvi/(?P<qtatDonada>(\d+\.\d+))/(?P<total>(\d+\.\d+))/$', views.donaCanvi, name='donaCanvi'),
    url(r'^donaCanvi/(?P<qtatDonada>\d+)/(?P<total>\d+)/$', views.donaCanvi, name='donaCanvi'),
    url(r'^donaCanvi/(?P<qtatDonada>\d+)/(?P<total>(\d+\.\d+))/$', views.donaCanvi, name='donaCanvi'),
    url(r'^donaCanvi/(?P<qtatDonada>(\d+\.\d+))/(?P<total>\d+)/$', views.donaCanvi, name='donaCanvi'),
 )
