# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-30 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trucker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('numbers', models.IntegerField()),
                ('product', models.CharField(max_length=100)),
            ],
        ),
    ]
