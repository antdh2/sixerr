# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-08 21:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sixerrapp', '0006_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='star',
            field=models.CharField(default=1, max_length=1),
            preserve_default=False,
        ),
    ]
