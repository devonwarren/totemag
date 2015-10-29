# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20151022_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publisher',
            field=models.ForeignKey(to='staff.Staff'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=autoslug.fields.AutoSlugField(populate_from='title', always_update=True, null=True, editable=True, unique=True),
        ),
    ]
