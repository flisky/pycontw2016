# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-04-27 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0002_auto_20160409_0442'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sponsor',
            options={'ordering': ('name',), 'verbose_name': 'sponsor', 'verbose_name_plural': 'sponsors'},
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='level',
            field=models.PositiveSmallIntegerField(choices=[(0, 'platinum'), (1, 'gold'), (2, 'silver'), (3, 'bronze'), (4, 'special')], verbose_name='level'),
        ),
    ]
