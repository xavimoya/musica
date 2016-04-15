# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0003_song_artista'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='artista',
            field=models.ForeignKey(to='imusica.Artist', null=True),
        ),
    ]
