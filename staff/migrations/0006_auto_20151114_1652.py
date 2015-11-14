# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0005_auto_20151105_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='instagram',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='pinterest',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='tumblr',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='youtube',
            field=models.URLField(null=True, blank=True),
        ),
    ]
