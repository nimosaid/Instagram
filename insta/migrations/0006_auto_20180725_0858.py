# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 08:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0005_auto_20180723_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]