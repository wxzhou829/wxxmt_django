# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pline', '0009_cost'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost',
            options={'ordering': ['-o_date'], 'verbose_name_plural': '其他费用表'},
        ),
        migrations.RenameField(
            model_name='cost',
            old_name='o_dat',
            new_name='o_date',
        ),
        migrations.AlterField(
            model_name='cost',
            name='qdj',
            field=models.IntegerField(default=0, verbose_name='汽单价'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='sdj',
            field=models.IntegerField(default=0, verbose_name='水单价'),
        ),
    ]
