# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('badsound', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='url',
            field=embed_video.fields.EmbedVideoField(verbose_name='URL (youtube, vimeo ou soundcloud)', unique=True),
        ),
    ]
