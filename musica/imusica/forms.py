from django.forms import ModelForm
from models import Artist, Song

class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        exclude = ('user', 'date',)

class SongForm(ModelForm):
    class Meta:
        model = Song
        exclude = ('user', 'date', 'artista')
