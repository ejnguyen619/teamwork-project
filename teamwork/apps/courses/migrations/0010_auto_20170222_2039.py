# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_auto_20170222_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='addCode',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
