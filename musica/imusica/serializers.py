from models import *
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

class CompanyiaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imusica:companyia-detail')
    #albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='imusica:album-detail')
    user = CharField(read_only=True)

    class Meta:
        model = Companyia
        fields = ('uri', 'name', 'city', 'website', 'user')

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imusica:artist-detail')
#    albums = HyperlinkedRelatedField(many=True, read_only=True, view_name='imusica:album-detail')
    companyia = HyperlinkedRelatedField(view_name='imusica:companyia-detail', read_only=True)

    class Meta:
        model = Artist
        fields = ('uri', 'name', 'city', 'country', 'website', 'idNumber', 'companyia')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imusica:album-detail')
    #songs = HyperlinkedRelatedField(many=True, read_only=True, view_name='imusica:song-detail')
    artista = HyperlinkedRelatedField(view_name='imusica:artist-detail', read_only=True)
    companyia = HyperlinkedRelatedField(view_name='imusica:companyia-detail', read_only=True)

    class Meta:
        model = Album
        fields = ('uri', 'name', 'idNumber', 'artista', 'companyia')

class SongSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='imusica:song-detail')
    name = CharField(read_only=True)
    artista = HyperlinkedRelatedField(view_name='imusica:artist-detail', read_only=True)
    album = HyperlinkedRelatedField(view_name='imusica:album-detail', read_only=True)

    class Meta:
        model = Song
        fields = ('uri', 'name', 'style', 'texte', 'artista', 'album')
