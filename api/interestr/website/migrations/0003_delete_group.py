# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 15:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_group_is_private'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
