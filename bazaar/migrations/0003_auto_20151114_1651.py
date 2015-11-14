# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0002_shop_submitted'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='facebook',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='instagram',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='pinterest',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='tumblr',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='twitter',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='shop',
            name='youtube',
            field=models.URLField(null=True, blank=True),
        ),
    ]
