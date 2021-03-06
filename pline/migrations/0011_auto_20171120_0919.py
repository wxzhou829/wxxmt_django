# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-20 09:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pline', '0010_auto_20171117_1627'),
    ]

    operations = [
        migrations.CreateModel(
            name='CostMonth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('o_date', models.CharField(default='201711', help_text='请输入年份和月份', max_length=6, verbose_name='日期')),
                ('jbf', models.IntegerField(default=0, verbose_name='加班费')),
                ('sf', models.IntegerField(default=0, verbose_name='水费')),
                ('zqf', models.IntegerField(default=0, verbose_name='蒸汽费')),
                ('lbf', models.IntegerField(default=0, verbose_name='劳保费')),
                ('bgf', models.IntegerField(default=0, verbose_name='办公费')),
                ('dzyh', models.IntegerField(default=0, verbose_name='低值易耗')),
                ('wlxh', models.IntegerField(default=0, verbose_name='物料消耗')),
                ('other', models.IntegerField(default=0, verbose_name='原料（药品）')),
                ('bzf', models.IntegerField(default=0, verbose_name='包装费')),
            ],
            options={
                'verbose_name_plural': '其他费用表(月)',
                'ordering': ['-o_date'],
            },
        ),
        migrations.AlterField(
            model_name='cost',
            name='qdj',
            field=models.IntegerField(default=408, verbose_name='汽单价'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='sdj',
            field=models.IntegerField(default=6, verbose_name='水单价'),
        ),
        migrations.AlterField(
            model_name='cost',
            name='wsf',
            field=models.IntegerField(default=57, verbose_name='污水费'),
        ),
    ]
