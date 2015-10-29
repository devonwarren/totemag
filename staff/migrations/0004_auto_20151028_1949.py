# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_staff_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='info_text',
            field=ckeditor.fields.RichTextField(help_text='Text to show under articles for author', blank=True),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(null=True, blank=True, upload_to='staff'),
        ),
    ]
