# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-19 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0010_auto_20180118_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursegrid',
            name='date_ini',
            field=models.DateField(default=django.utils.timezone.now, null=True, verbose_name='data in\xedcio'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='date_term',
            field=models.DateField(blank=True, null=True, verbose_name='data t\xe9rmino'),
        ),
    ]
