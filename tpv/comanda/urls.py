# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from comanda import views

urlpatterns = patterns('',
    url(r'^$', views.llistarComandes, name='llistarComandes'),
)
