# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-04-23 00:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tether', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchplayers',
            name='player1_id',
            field=models.BigIntegerField(null=True),
        ),
    ]
