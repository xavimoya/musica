# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0004_album_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(to='imusica.Album', null=True),
        ),
    ]
