# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_auto_20151101_1325'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ArticleCategory',
            new_name='Category',
        ),
    ]
