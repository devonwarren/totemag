# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_article_publish_after'),
        ('advertising', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='adimage',
            name='categories',
            field=models.ManyToManyField(to='articles.Category'),
        ),
    ]