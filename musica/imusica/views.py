from django.shortcuts import HttpResponse, render_to_response
from models import *
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.core import serializers
from django.views.generic.base import TemplateResponseMixin
from django.views.generic import ListView, DetailView

def mainpage(request):
    return HttpResponse("<ul><h2>Hola!</h2>    <p>Hauries de entrar al /app per accedir a l'aplicacio<br>"
                            "/admin per entrar com administrador<br>"
                            "/accounts/(login|logout) per entrar o sortir<br><br</p></ul>"
                            " <ul><u>Aqui tens els Links:</u></ul>"
                            "<ul><p><a href= 'app' > Aplicacio</a> <br>"
                            "<a href= 'admin' > Administrador</a><br>"
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

class Inici(ListView):
    model = Artist
    template_name = 'index.html'
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

class ArtistDetail(DetailView):
    model = Artists
    template_name = 'artist_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        return context
