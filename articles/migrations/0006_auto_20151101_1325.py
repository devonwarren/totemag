# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_auto_20151030_1141'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('parent', models.ForeignKey(to='articles.ArticleCategory', related_name='children', null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(verbose_name='URL', editable=False, populate_from='title', always_update=True, help_text="URL for page details ('/article/URL')", null=True, unique=True),
        ),
    ]
