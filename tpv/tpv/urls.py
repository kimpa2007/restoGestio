from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^gestio/', include('gestio.urls', namespace='gestio')),
    url(r'^usuaris/', include('usuaris.urls', namespace='usuaris')),
    url(r'^productes/', include('productes.urls', namespace='productes')),
    url(r'^comandes/', include('comanda.urls', namespace='comandes')),
    url(r'^tpv/', include('passaComanda.urls', namespace='tpv')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
