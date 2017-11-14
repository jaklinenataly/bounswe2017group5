# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-14 23:41
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DataTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('fields', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
            options={
                'ordering': ('created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField(blank=True, default='')),
                ('location', models.TextField(blank=True, default='')),
                ('tags', models.TextField(blank=True, default='')),
                ('is_private', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(default='')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField(default=None, null=True)),
                ('data_template', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.DataTemplate')),
                ('group', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.Group')),
                ('owner', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('created',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('label', models.CharField(max_length=40)),
                ('url', models.SlugField()),
                ('concept_uri', models.SlugField(primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'ordering': ('created',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='datatemplate',
            name='group',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data_templates', to='api.Group'),
        ),
        migrations.AddField(
            model_name='datatemplate',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='data_templates', to=settings.AUTH_USER_MODEL),
        ),
    ]
