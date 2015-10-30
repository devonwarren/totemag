# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_image_attribution'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(verbose_name='URL', null=True, always_update=True, populate_from='title', help_text="URL for page details ('/article/URL')", editable=True, unique=True),
        ),
    ]
