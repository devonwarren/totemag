# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bazaar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='submitted',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 30, 15, 41, 49, 388570, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
