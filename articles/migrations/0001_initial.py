# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import ckeditor.fields
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', autoslug.fields.AutoSlugField(null=True, populate_from='title', always_update=True, unique=True, editable=False)),
                ('image', models.ImageField(upload_to='journal')),
                ('body', ckeditor.fields.RichTextField()),
                ('published_date', models.DateField()),
                ('publisher', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
