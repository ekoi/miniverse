# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 19:49
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Installation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lat', models.DecimalField(decimal_places=6, default=Decimal('0.0000'), max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, default=Decimal('0.0000'), max_digits=9)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('marker', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('description', models.TextField(blank=True, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('version', models.CharField(blank=True, max_length=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('lat', models.DecimalField(decimal_places=6, default=Decimal('0.0000'), max_digits=9)),
                ('lng', models.DecimalField(decimal_places=6, default=Decimal('0.0000'), max_digits=9)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='installations.Installation')),
            ],
        ),
    ]
