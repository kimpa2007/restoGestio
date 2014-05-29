# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from passaComanda import views

urlpatterns = patterns('',
    url(r'^$', views.pintatpv, name='pintatpv'),
    url(r'^donaTaules/$', views.donaTaules, name='donaTaules'),
    url(r'^passaComanda/$', views.passaComanda, name='passaComanda'),
)
