# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 01:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('advertising', '0002_adimage_categories'), ('advertising', '0003_auto_20160224_2021')]

    dependencies = [
        ('articles', '0019_article_publish_after'),
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adimage',
            name='caption',
            field=models.CharField(default='', max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adimage',
            name='url',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
