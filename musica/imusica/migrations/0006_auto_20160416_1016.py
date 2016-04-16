# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0005_song_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='idNumber',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
