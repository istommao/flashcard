# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-05 10:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='short_intro',
            field=models.CharField(default='', max_length=512, verbose_name='简介'),
            preserve_default=False,
        ),
    ]
