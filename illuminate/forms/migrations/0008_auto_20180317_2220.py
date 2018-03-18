# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-17 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_auto_20180317_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(help_text='Enter Your Full Name.', max_length=128)),
                ('lc', models.CharField(choices=[(1489, 'New Cairo'), (1727, 'Menofia'), (1729, 'Assiut'), (2126, 'Beni Suef'), (2114, 'Luxor & Aswan'), (1730, 'Sohag'), (2124, 'Helwan'), (15, 'Suez'), (171, 'Mansoura'), (257, 'GUC'), (1726, 'Fayoum'), (1322, 'AAST In CAIRO'), (109, 'Damietta'), (152, '6TH OCTOBER'), (1788, 'AAST Alexandria'), (899, 'Alexandria'), (1789, 'Ain Shams University'), (2125, 'MIU'), (1114, 'Zagazig'), (1064, 'Cairo University'), (1728, 'Minya'), (2387, 'MC Egypt'), (1725, 'Tanta')], max_length=1, null=True)),
                ('position', models.CharField(choices=[('MCP', 'MCP'), ('MCVP', 'MCVP'), ('LCP', 'LCP'), ('LCVP', 'LCVP'), ('Team Leader', 'Team Leader'), ('Coordinator', 'Coordinator'), ('Member', 'Member')], max_length=1, null=True)),
                ('role', models.CharField(blank=True, choices=[('IGV', 'IGV'), ('IGE', 'IGE'), ('IGT', 'IGT'), ('OGV', 'OGV'), ('OGE', 'OGE'), ('OGT', 'OGT'), ('F&L', 'F&L'), ('TM', 'TM'), ('Marketing', 'Marketing')], max_length=1, null=True)),
                ('ep_name', models.CharField(help_text="Enter EP's Full Name.", max_length=128)),
                ('ep_entity', django_countries.fields.CountryField(max_length=2, null=True)),
                ('ep_email', models.EmailField(max_length=254)),
                ('ep_lc', models.CharField(choices=[(1489, 'New Cairo'), (1727, 'Menofia'), (1729, 'Assiut'), (2126, 'Beni Suef'), (2114, 'Luxor & Aswan'), (1730, 'Sohag'), (2124, 'Helwan'), (15, 'Suez'), (171, 'Mansoura'), (257, 'GUC'), (1726, 'Fayoum'), (1322, 'AAST In CAIRO'), (109, 'Damietta'), (152, '6TH OCTOBER'), (1788, 'AAST Alexandria'), (899, 'Alexandria'), (1789, 'Ain Shams University'), (2125, 'MIU'), (1114, 'Zagazig'), (1064, 'Cairo University'), (1728, 'Minya'), (2387, 'MC Egypt'), (1725, 'Tanta')], max_length=1, null=True)),
                ('ep_id', models.IntegerField(help_text='Enter EP ID.')),
                ('opp_id', models.IntegerField(help_text='Enter Opportunity ID.')),
                ('requested_break', models.CharField(choices=[('Approval', 'Approval'), ('Realization', 'Realization')], max_length=1, null=True)),
                ('program', models.CharField(choices=[('GV', 'Global Volunteer'), ('GE', 'Global Entrepreneur'), ('GT', 'Global Talent')], max_length=1, null=True)),
                ('request_Reason', models.TextField(help_text='Detailed yet to the point for us to help you best!')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='complaint',
            name='host_lc',
            field=models.CharField(choices=[(1489, 'New Cairo'), (1727, 'Menofia'), (1729, 'Assiut'), (2126, 'Beni Suef'), (2114, 'Luxor & Aswan'), (1730, 'Sohag'), (2124, 'Helwan'), (15, 'Suez'), (171, 'Mansoura'), (257, 'GUC'), (1726, 'Fayoum'), (1322, 'AAST In CAIRO'), (109, 'Damietta'), (152, '6TH OCTOBER'), (1788, 'AAST Alexandria'), (899, 'Alexandria'), (1789, 'Ain Shams University'), (2125, 'MIU'), (1114, 'Zagazig'), (1064, 'Cairo University'), (1728, 'Minya'), (2387, 'MC Egypt'), (1725, 'Tanta')], max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='program',
            field=models.CharField(choices=[('GV', 'Global Volunteer'), ('GE', 'Global Entrepreneur'), ('GT', 'Global Talent')], max_length=128, null=True),
        ),
    ]
