# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180422_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Position'),
        ),
    ]
