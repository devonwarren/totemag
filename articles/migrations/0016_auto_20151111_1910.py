# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_auto_20151105_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('-published_date',)},
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='articles', help_text='Image used on homepage grid,         also shown at top of the page unless there are slideshow images'),
        ),
        migrations.AlterField(
            model_name='slideshowimage',
            name='description',
            field=models.TextField(),
        ),
    ]
