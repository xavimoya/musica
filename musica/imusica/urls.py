from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse_lazy
from django.views.generic.base import RedirectView
from django.conf.urls import include, url, patterns
from django.contrib import admin
from views import *
from models import *
from rest_framework.urlpatterns import format_suffix_patterns



admin.autodiscover()

urlpatterns = patterns('',

url(r'^$',Inici.as_view(),),
url(r'^api/$', IniciApiRest.as_view(),),

#List models
# ex html: /app/Artist
# ex xml: /app/Artist.xml
# ex json: /app/Artist.json
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

#	DETALLS de cada artista

    # Artist details, ex: /app/Artist/1.json
    url(r'^Artist/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        ArtistDetail.as_view(),
        name='artist_detail'),

    # Create an artist, ex /app/Artist/create
    url(r'^Artist/create/$',
        ArtistCreate.as_view(),
        name='artist_create'),

    # Edit artist details, ex /app/Artist/1/edit
    url(r'^Artist/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Artist,
            form_class=ArtistForm),
        name='artist_edit'),

#	DETALLS de cada canso

	# SONGS details, ex.: /app/Song/1.json
    url(r'^Song/(?P<pk>\d+)(\.(?P<extension>(json|xml)))$',
        SongDetail.as_view(),
        name='song_detail'),

    # Create a song, ex: /app/Song/create/
    url(r'^Song/create/$',
        SongCreate.as_view(),
        name='song_create'),

    # Edit an artist song details, ex: /app/Artist/1/Song/1/edit/
    url(r'^Artist/(?P<pkr>\d+)/Song/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Song,
            form_class=SongForm),
        name='song_edit'),
    # Create an artist review using function, ex: /app/Artist/1/reviews/create/
    url(r'^Artist/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),
        
        
## Songs of Artist

	# Artist songs list, ex.: /app/Artist/1/Song.json
    url(r'^Artist/(?P<pk>\d+)/Song\.(?P<extension>(json|xml))$',
        SongList.as_view(),
        name='song_list'),

    # Artist song details, ex.: /app/Artist/1/Song/1.json
    url(r'^Artist/(?P<pkr>\d+)/Song/(?P<pk>\d+)(\.(?P<extension>(json|xml)))?$',
        SongDetail.as_view(),
        name='song_detail'),

    # Create a artist song, ex: /app/Artist/1/Song/create/
    url(r'^Artist/(?P<pk>\d+)/Song/create/$',
        SongCreate.as_view(),
        name='song_create'),

    # Edit an artist song details, ex: /app/Artist/1/Song/1/edit/
    url(r'^Artist/(?P<pkr>\d+)/Song/(?P<pk>\d+)/edit/$',
        LoginRequiredCheckIsOwnerUpdateView.as_view(
            model=Song,
            form_class=SongForm),
        name='song_edit'),
    # Create an artist review using function, ex: /app/Artist/1/reviews/create/
    url(r'^Artist/(?P<pk>\d+)/reviews/create/$',
        review,
        name='review_create'),


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
    url(r'^api/Artistreviews/$',
        APIArtistReviewList.as_view(), name='artistreview-list'),
    url(r'^api/Artistreviews/(?P<pk>\d+)/$',
        APIArtistReviewDetail.as_view(), name='artistreview-detail'),

]

# Format suffixes
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api','json', 'xml'])
