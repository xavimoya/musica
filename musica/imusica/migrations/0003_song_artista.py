# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0002_auto_20160414_1726'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artista',
            field=models.ForeignKey(to='imusica.Artist', null=True),
        ),
    ]
