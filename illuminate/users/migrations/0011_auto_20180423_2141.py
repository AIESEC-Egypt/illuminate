# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-23 19:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20180423_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='uploads/default_image.png', upload_to='uploads/'),
        ),
    ]
