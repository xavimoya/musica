from models import *
from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer

class CompanyiaSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='companya-detail')
    class Meta:
        model = Companyia
        fields = ('uri', 'name', 'city', 'website')

class ArtistSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='artist-detail')

    class Meta:
        model = Artist
        fields = ('uri', 'name', 'city', 'country', 'website', 'idNumber', 'companyia')

class AlbumSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='album-detail')

    class Meta:
        model = Album
        fields = ('uri', 'name', 'idNumber', 'artista', 'companyia')

class SongSerializer(HyperlinkedModelSerializer):
    uri = HyperlinkedIdentityField(view_name='song-detail')
    name = CharField(read_only=True)

    class Meta:
        model = Song
        fields = ('uri', 'name', 'style', 'texte', 'artista', 'album')
