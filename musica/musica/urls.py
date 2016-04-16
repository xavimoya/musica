
from django.conf.urls import include, url
from django.contrib import admin
from imusica.views import *
from imusica.models import *
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^$',mainpage),

    url(r'^admin/',include(admin.site.urls)),
    url(r'^app/', include('imusica.urls', namespace='imusica')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name = 'logout'),

]
