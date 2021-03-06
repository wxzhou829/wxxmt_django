# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-28 09:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pline', '0014_auto_20171127_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('pg3', models.IntegerField(default=0, verbose_name='滚一线')),
                ('pg2a', models.IntegerField(default=0, verbose_name='滚二线A')),
                ('pg2c', models.IntegerField(default=0, verbose_name='滚二线C')),
                ('pg2d', models.IntegerField(default=0, verbose_name='滚二线D')),
                ('pd3', models.IntegerField(default=0, verbose_name='吊镀线')),
                ('plat_5m', models.IntegerField(default=0, verbose_name='五米平台')),
                ('f_toilet', models.IntegerField(default=0, verbose_name='前面厕所')),
                ('b_toilet', models.IntegerField(default=0, verbose_name='后面厕所')),
                ('b_roof', models.IntegerField(default=0, verbose_name='后楼顶')),
                ('lab', models.IntegerField(default=0, verbose_name='实验室')),
                ('final_water', models.IntegerField(default=0, verbose_name='终水')),
                ('pure_water', models.IntegerField(default=0, verbose_name='纯水')),
                ('main_water', models.IntegerField(default=0, verbose_name='总表（外）')),
                ('main_water_n', models.IntegerField(default=0, verbose_name='总表（内）')),
            ],
            options={
                'verbose_name_plural': '水表',
                'ordering': ['-date'],
            },
        ),
        migrations.AlterModelOptions(
            name='guzhang',
            options={'verbose_name_plural': '故障'},
        ),
        migrations.AlterModelOptions(
            name='quandata',
            options={'ordering': ['-date'], 'verbose_name_plural': '全检数据'},
        ),
        migrations.AlterModelOptions(
            name='yao',
            options={'verbose_name_plural': '药水'},
        ),
        migrations.AlterField(
            model_name='quandata',
            name='quanjian',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pline.Quanjian', verbose_name='全检件号'),
        ),
    ]
