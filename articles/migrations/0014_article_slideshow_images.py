# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0013_slideshowimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slideshow_images',
            field=models.ManyToManyField(to='articles.SlideshowImage', null=True, blank=True),
        ),
    ]
