# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0014_article_slideshow_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='slideshow_images',
        ),
        migrations.AddField(
            model_name='slideshowimage',
            name='article',
            field=models.ForeignKey(to='articles.Article', default=''),
            preserve_default=False,
        ),
    ]
