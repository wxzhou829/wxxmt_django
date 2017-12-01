# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pline', '0006_jiapd3'),
    ]

    operations = [
        migrations.CreateModel(
            name='JiaPG2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('sc30', models.IntegerField(default=0, verbose_name='SC-30')),
                ('hcl', models.IntegerField(default=0, verbose_name='HCL')),
                ('rc30', models.IntegerField(default=0, verbose_name='RC-30')),
                ('rc25st', models.IntegerField(default=0, verbose_name='RC-25ST')),
                ('ds31', models.IntegerField(default=0, verbose_name='DS-31')),
                ('naoh', models.IntegerField(default=0, verbose_name='NAOH')),
                ('xb', models.IntegerField(default=0, verbose_name='锌板')),
                ('lj', models.IntegerField(default=0, verbose_name='粒碱')),
                ('nz200r', models.IntegerField(default=0, verbose_name='NZ-200R')),
                ('nzrba', models.IntegerField(default=0, verbose_name='NZ-RBA')),
                ('h0616y', models.IntegerField(default=0, verbose_name='H-0616Y')),
                ('hztzj', models.IntegerField(default=0, verbose_name='HZ调整剂')),
                ('j441a', models.IntegerField(default=0, verbose_name='441A加药量')),
                ('j444cs', models.IntegerField(default=0, verbose_name='444CS加药量')),
                ('j444cst', models.IntegerField(default=0, verbose_name='444CST加药量')),
                ('j447md1', models.IntegerField(default=0, verbose_name='447MD1加药量')),
                ('j447md2', models.IntegerField(default=0, verbose_name='447MD2加药量')),
                ('j447md3', models.IntegerField(default=0, verbose_name='447MD3加药量')),
                ('j447md4', models.IntegerField(default=0, verbose_name='447MD4加药量')),
                ('j447md7', models.IntegerField(default=0, verbose_name='447MD7加药量')),
                ('j118', models.IntegerField(default=0, verbose_name='ZTB-118加药量')),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name_plural': 'PG2加药表',
            },
        ),
        migrations.AlterModelOptions(
            name='jiapd3',
            options={'ordering': ['-date'], 'verbose_name_plural': 'PD3加药表'},
        ),
    ]