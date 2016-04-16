from django.conf.urls import include, url, patterns
from django.contrib import admin
from imusica.views import *
from imusica.models import *


admin.autodiscover()

urlpatterns = patterns('',

url(r'^$',Inici.as_view(),),


url(r'^Artist.json/$',artistjson, name='artist_list'),
url(r'^Artist.xml/$',artistxml, name='artist_list'),
url(r'^Artist/$',Artists.as_view(), name='artist_list'),
url(r'^Album.json/$',albumjson, name='album_list'),
url(r'^Album.xml/$',albumxml, name='album_list'),
url(r'^Album/$',Albums.as_view(), name='album_list'),
url(r'^Song.json/$',songjson, name='song_list'),
url(r'^Song.xml/$',songxml, name='song_list'),
url(r'^Song/$',Songs.as_view(), name='song_list'),
url(r'^Companyia.json/$',companyiajson, name='companyia_list'),
url(r'^Companyia.xml/$',companyiaxml, name='companyia_list'),
url(r'^Companyia/$',Companyies.as_view(), name='companyia_list'),
#

)
