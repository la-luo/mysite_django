# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-09 01:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0019_auto_20180508_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='num',
            field=models.IntegerField(null=True),
        ),
    ]
