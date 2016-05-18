
from django.conf.urls import include, url
from django.contrib import admin
from imusica.views import *
from imusica.models import *
from django.contrib.auth.views import login, logout
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    url(r'^$',mainpage),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^app/', include('imusica.urls', namespace='imusica')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name = 'logout'),

]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, })
    ]
