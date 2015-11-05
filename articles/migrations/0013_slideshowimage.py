# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_category_allow_select'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlideshowImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('image', models.ImageField(upload_to='articles')),
                ('description', models.CharField(max_length=250)),
            ],
        ),
    ]
