# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('month', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='theme',
            name='month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')]),
        ),
        migrations.AlterField(
            model_name='theme',
            name='year',
            field=models.IntegerField(choices=[(2015, 2015), (2016, 2016), (2017, 2017)]),
        ),
    ]