# Uncomment the next two lines to enable the admin:
from django.conf.urls import patterns, include, url
from productes import views

urlpatterns = patterns('',
    url(r'^$', views.llistarProductes, name='llistarProductes'),
    url(r'^llistarCategories/$', views.llistarCategories, name='llistarCategories'),
    url(r'^llistarProductes/$', views.llistarProductes, name='llistarProductes'),
    url(r'^afegirProducte/(?P<categoria>\w+)/$', views.afegirProducte, name='afegirProducte'),
    url(r'^afegirProducte/$', views.afegirProducte, name='afegirProducte'),   
    url(r'^afegirCategoria/$', views.afegirCategoria, name='afegirCategoria'),   
    url(r'^editarProducte/(?P<idProducte>\d+)/$', views.editarProducte, name='editarProducte'),
    
 )

