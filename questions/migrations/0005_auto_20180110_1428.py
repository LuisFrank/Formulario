# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 14:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20180110_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statementtest',
            name='answer_value',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
