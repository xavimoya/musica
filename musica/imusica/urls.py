from django.conf.urls import include, url, patterns
from django.contrib import admin
from views import *
from models import *
from rest_framework.urlpatterns import format_suffix_patterns



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

### RESTful urls

urlpatterns += [
        url(r'^api/auth/',
        include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/Companyia/$',
        APICompanyiaList.as_view(), name='companyia-list'),
    url(r'^api/Companyia/(?P<pk>\d+)/$',
        APICompanyiaDetail.as_view(), name='companyia-detail'),
    url(r'^api/Artist/$',
        APIArtistList.as_view(), name='artist-list'),
    url(r'^api/Artist/(?P<pk>\d+)/$',
        APIArtistDetail.as_view(), name='artist-detail'),
    url(r'^api/Album/$',
        APIAlbumList.as_view(), name='album-list'),
    url(r'^api/Album/(?P<pk>\d+)/$',
        APIAlbumDetail.as_view(), name='album-detail'),
    url(r'^api/Song/$',
        APISongList.as_view(), name='song-list'),
    url(r'^api/Song/(?P<pk>\d+)/$',
        APISongDetail.as_view(), name='song-detail'),

]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
