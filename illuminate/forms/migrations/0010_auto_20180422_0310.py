# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-22 01:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0009_auto_20180422_0219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='ep',
            name='ep_lc',
            field=models.CharField(blank=True, help_text='Enter lc Name.', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='case_brief',
            field=models.TextField(help_text='Detailed yet to the point', null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='case_mail_subject',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='standards',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forms.Standard'),
        ),
    ]
