# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-18 20:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_auto_20180118_1425'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='enrollment',
            options={'verbose_name': 'Encargo', 'verbose_name_plural': 'Encargos'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='observations',
            field=models.TextField(null=True, verbose_name='observa\xe7\xf5es'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='campus',
            name='phone2',
            field=models.CharField(max_length=14, null=True, verbose_name='telefone 2'),
        ),
        migrations.AlterField(
            model_name='contracttype',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='course',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='coursegrid',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='active',
            field=models.BooleanField(default=True, verbose_name='ativo'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='efetivo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone2',
            field=models.CharField(max_length=14, null=True, verbose_name='telefone 2'),
        ),
    ]