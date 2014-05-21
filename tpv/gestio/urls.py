# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from gestio import views

urlpatterns = patterns('',
    url(r'^$', views.menu, name='menu'),
    url(r'^dataHora/$', views.dataHora, name='dataHora'),
 )
