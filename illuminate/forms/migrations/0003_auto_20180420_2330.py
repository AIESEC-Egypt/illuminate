# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-20 21:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0002_auto_20180419_1923'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filler',
            old_name='Filler_lc',
            new_name='filler_lc',
        ),
        migrations.AddField(
            model_name='ticket',
            name='filler',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Filler'),
        ),
    ]
