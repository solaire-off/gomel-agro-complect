# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-16 12:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='published',
            field=models.BooleanField(default=1, verbose_name='Опубликована'),
        ),
    ]
