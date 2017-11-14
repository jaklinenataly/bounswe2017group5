# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 18:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('api', '0010_datatemplate'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='data_template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.DataTemplate'),
        ),
        migrations.AddField(
            model_name='post',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.Group'),
        ),
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
