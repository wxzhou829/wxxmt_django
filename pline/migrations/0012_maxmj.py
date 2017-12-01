# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pline', '0011_auto_20171120_0919'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaxMJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yao', models.CharField(choices=[('1', '441A'), ('2', '444CS'), ('3', '447MD'), ('4', '124'), ('5', '444s'), ('5', '447s')], max_length=1, verbose_name='药水')),
                ('maxV', models.IntegerField(default=0, verbose_name='最大值')),
            ],
        ),
    ]