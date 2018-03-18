# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20180317_2109'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AccessToken',
        ),
        migrations.AlterField(
            model_name='complaint',
            name='host_lc',
            field=models.CharField(choices=[(1489, 'New Cairo'), (1727, 'Menofia'), (1729, 'Assiut'), (2126, 'Beni Suef'), (2114, 'Luxor & Aswan'), (1730, 'Sohag'), (2124, 'Helwan'), (15, 'Suez'), (171, 'Mansoura'), (257, 'GUC'), (1726, 'Fayoum'), (1322, 'AAST In CAIRO'), (109, 'Damietta'), (152, '6TH OCTOBER'), (1788, 'AAST Alexandria'), (899, 'Alexandria'), (1789, 'Ain Shams University'), (2125, 'MIU'), (1114, 'Zagazig'), (1064, 'Cairo University'), (1728, 'Minya'), (2387, 'MC Egypt'), (1725, 'Tanta')], help_text='Choose Host LC', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='program',
            field=models.CharField(choices=[('GV', 'Global Volunteer'), ('GE', 'Global Entrepreneur'), ('GT', 'Global Talent')], help_text='Choose Program', max_length=128, null=True),
        ),
    ]
