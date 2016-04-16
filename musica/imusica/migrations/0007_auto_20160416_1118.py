# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0006_auto_20160416_1016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companyia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('website', models.URLField(blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='title',
        ),
        migrations.AddField(
            model_name='song',
            name='style',
            field=models.CharField(default=b'Pop', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='texte',
            field=models.CharField(default=b'Lletra completa', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='album',
            name='companyia',
            field=models.ForeignKey(to='imusica.Companyia', null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='companyia',
            field=models.ForeignKey(to='imusica.Companyia', null=True),
        ),
    ]
