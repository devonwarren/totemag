# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_featured'),
        ('articles', '0003_auto_20151027_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_attribution',
            field=models.ForeignKey(related_name='image_attribution', blank=True, to='staff.Staff', null=True),
        ),
    ]
