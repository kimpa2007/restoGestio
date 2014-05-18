# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from productes import views

urlpatterns = patterns('',
    url(r'^$', views.llistarProductes, name='llistarProductes'),
    url(r'^llistarCategories/$', views.llistarCategories, name='llistarCategories'),
 )
