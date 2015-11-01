# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0011_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='allow_select',
            field=models.BooleanField(help_text='Allow articles to be added to this category', default=True),
        ),
    ]
