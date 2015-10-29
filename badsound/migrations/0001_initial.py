# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('url', embed_video.fields.EmbedVideoField(unique=True, verbose_name='URL')),
                ('title', models.TextField(verbose_name='Titre')),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('music1', models.ForeignKey(to='badsound.Music', related_name='vote1')),
                ('music2', models.ForeignKey(to='badsound.Music', related_name='vote2')),
                ('winner', models.ForeignKey(to='badsound.Music')),
            ],
        ),
    ]
