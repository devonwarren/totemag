# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('image1', models.ImageField(upload_to='bazaar')),
                ('image2', models.ImageField(upload_to='bazaar', null=True, blank=True)),
                ('body', ckeditor.fields.RichTextField()),
            ],
        ),
    ]
