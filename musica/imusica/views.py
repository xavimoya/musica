from django.shortcuts import HttpResponse, render_to_response, get_object_or_404
from models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.core import serializers
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import ListView, DetailView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import *
from serializers import *
from forms import *
from django.utils.decorators import method_decorator
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView


def mainpage(request):
    return HttpResponse("<ul><h2>Hola!</h2>    <p>Hauries de entrar a: <br>"
                            "/app per accedir a l'aplicacio<br>"
                            "/admin per entrar com administrador<br>"
                            "/app/api per entrar a l'API RESTful<br>"
                            "/accounts/(login|logout) per entrar o sortir<br><br</p></ul>"
                            " <ul><u>Aqui tens els Links:</u></ul>"
                            "<ul><p><a href= 'app' > Aplicacio</a> <br>"
                            "<a href= 'admin' > Administrador</a><br>"
                            "<a href= 'app/api' > API</a><br>"
                            "<a href= 'accounts/login' > Log in</a><br>"
                            "<a href= 'accounts/logout' > Logout</a><br></p></ul>")


class ConnegResponseMixin(TemplateResponseMixin):

    def render_json_object_response(self, objects, **kwargs):
        json_data = serializers.serialize(u"json", objects, **kwargs)
        return HttpResponse(json_data, content_type=u"application/json")

    def render_xml_object_response(self, objects, **kwargs):
        xml_data = serializers.serialize(u"xml", objects, **kwargs)
        return HttpResponse(xml_data, content_type=u"application/xml")

    def render_to_response(self, context, **kwargs):
        if 'extension' in self.kwargs:
            try:
                objects = [self.object]
            except AttributeError:
                objects = self.object_list
            if self.kwargs['extension'] == 'json':
                return self.render_json_object_response(objects=objects)
            elif self.kwargs['extension'] == 'xml':
                return self.render_xml_object_response(objects=objects)
        return super(ConnegResponseMixin, self).render_to_response(context)

class LoginRequiredMixin(object):
    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)

class CheckIsOwnerMixin(object):
    def get_object(self, *args, **kwargs):
        obj = super(CheckIsOwnerMixin, self).get_object(*args, **kwargs)
        if not obj.user == self.request.user:
            raise PermissionDenied
        return obj

class LoginRequiredCheckIsOwnerUpdateView(LoginRequiredMixin, CheckIsOwnerMixin, UpdateView):
    template_name = 'form.html'

class Inici(ListView):
    model = Artist
    template_name = 'index.html'
    queryset = Artist.objects.all()

class IniciApiRest(ListView):
    template_name = 'index2.html'
    queryset = Artist.objects.all()

class Artists(ListView, ConnegResponseMixin):
    model = Artist
    template_name = 'artists.html'
    queryset = Artist.objects.all()
    context_object_name = 'artist_list'

def artistjson(request):
    model = Artist
    queryset = Artist.objects.all()
    data = serializers.serialize('json',queryset)
    return HttpResponse(data, content_type='application/json')

def artistxml(request):
    model = Artist
    queryset = Artist.objects.all()
    data = serializers.serialize('xml',queryset)
    return HttpResponse(data, content_type='application/xml')


class Albums(ListView, ConnegResponseMixin):
    model = Album
    template_name = 'albums.html'
    queryset = Album.objects.all()
    context_object_name = 'album_list'

def albumjson(request):
    model = Album
    queryset = Album.objects.all()
    data = serializers.serialize('json',queryset)
    return HttpResponse(data, content_type='application/json')

def albumxml(request):
    model = Album
    queryset = Album.objects.all()
    data = serializers.serialize('xml',queryset)
    return HttpResponse(data, content_type='application/xml')



class Songs(ListView, ConnegResponseMixin):
    model = Song
    template_name = 'songs.html'
    queryset = Song.objects.all()
    context_object_name = 'song_list'

def songjson(request):
    model = Song
    queryset = Song.objects.all()
    data = serializers.serialize('json',queryset)
    return HttpResponse(data, content_type='application/json')

def songxml(request):
    model = Song
    queryset = Song.objects.all()
    data = serializers.serialize('xml',queryset)
    return HttpResponse(data, content_type='application/xml')

class Companyies(ListView, ConnegResponseMixin):
    model = Companyia
    template_name = 'companyies.html'
    queryset = Companyia.objects.all()
    context_object_name = 'companyia_list'

def companyiajson(request):
    model = Companyia
    queryset = Companyia.objects.all()
    data = serializers.serialize('json',queryset)
    return HttpResponse(data, content_type='application/json')

def companyiaxml(request):
    model = Companyia
    queryset = Companyia.objects.all()
    data = serializers.serialize('xml',queryset)
    return HttpResponse(data, content_type='application/xml')



### Detail - Create //Artist
class ArtistDetail(DetailView, ConnegResponseMixin):
    model = Artist
    template_name = 'artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context

class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    template_name = 'form.html'
    form_class = ArtistForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(ArtistCreate, self).form_valid(form)

### List - Detail - Create //Song of an Artist

class SongList(ListView, ConnegResponseMixin):
    model = Song

    def get_queryset(self):
        return Song.objects.filter(artist=self.kwargs['pk'])

class SongDetail(DetailView, ConnegResponseMixin):
    model = Song
    template_name = 'song_detail.html'

class SongCreate(LoginRequiredMixin, CreateView):
    model = Song
    template_name = 'form.html'
    form_class = SongForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        #form.instance.artista = Artist.objects.get(id=self.kwargs['pk'])
        return super(SongCreate, self).form_valid(form)



### RESTful API views
class IsOwnerOrReadOnly(permissions.IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        # Instance must have an attribute named `owner`.
        return obj.user == request.user


class APICompanyiaList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Companyia
    queryset = Companyia.objects.all()
    serializer_class = CompanyiaSerializer

class APICompanyiaDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Companyia
    queryset = Companyia.objects.all()
    serializer_class = CompanyiaSerializer

class APIArtistList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIArtistDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Artist
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer

class APIAlbumList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APIAlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Album
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class APISongList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer

class APISongDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    model = Song
    queryset = Song.objects.all()
    serializer_class = SongSerializer
