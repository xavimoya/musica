from django.contrib import admin

# Register your models here.
#from imusica.models import *

#admin.site.register(Companyia)
#admin.site.register(Artist)
#admin.site.register(Album)
#admin.site.register(Song)

import models

admin.site.register(models.Companyia)
admin.site.register(models.Artist)
admin.site.register(models.Album)
admin.site.register(models.Song)
