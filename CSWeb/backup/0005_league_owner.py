# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-03-31 07:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tether', '0004_remove_league_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='league',
            name='owner',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
