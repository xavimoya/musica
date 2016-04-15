# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imusica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('idNumber', models.TextField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='artist',
            name='city',
            field=models.CharField(default=b'City', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='country',
            field=models.CharField(default=b'Country', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='idNumber',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='artist',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='texte',
            field=models.CharField(default=b'Valor S3', max_length=50, blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default=b'Valor S2', max_length=50, blank=True),
        ),
    ]
