# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20151027_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='featured',
            field=models.BooleanField(help_text='Show on About page', default=False),
        ),
    ]
