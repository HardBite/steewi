# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-11 14:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170311_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcomment',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
