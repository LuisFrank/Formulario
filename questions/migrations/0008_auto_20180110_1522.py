# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-10 15:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_statement'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statement',
            old_name='text',
            new_name='title',
        ),
    ]
