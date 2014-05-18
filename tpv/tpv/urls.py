from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gestio/', include('gestio.urls', namespace='gestio')),
    url(r'^usuaris/', include('usuaris.urls', namespace='usuaris')),
    url(r'^productes/', include('productes.urls', namespace='productes')),
    #url(r'^comandes/', include('comandes.urls', namespace='comandes')),

)
