# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-09-20 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('installations', '0006_auto_20160920_1027'),
    ]

    operations = [
        migrations.AddField(
            model_name='installation',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Show on map?'),
        ),
        migrations.AlterField(
            model_name='installation',
            name='slug',
            field=models.SlugField(blank=True, help_text='auto-filled on save', max_length=255),
        ),
    ]
