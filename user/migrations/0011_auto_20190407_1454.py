# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2019-04-07 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_auto_20190407_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file_classify',
            field=models.CharField(default='普通文档', max_length=32, verbose_name='文件分类'),
        ),
    ]