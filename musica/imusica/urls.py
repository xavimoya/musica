from django.conf.urls import include, url, patterns
from django.contrib import admin
from imusica.views import *
from imusica.models import *

admin.autodiscover()

urlpatterns = patterns('',

url(r'^$',Inici.as_view(),),
url(r'^Artist/$',Artists.as_view(), name='artist_list'),
url(r'^Artist\.(?P<extension>(json|xml))$', Artists.as_view(), name='artist_list_resp'),



)
