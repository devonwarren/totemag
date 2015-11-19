# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0016_auto_20151111_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slideshowimage',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
