# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 00:28
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import notice.models


class Migration(migrations.Migration):

    dependencies = [
        ('notice', '0002_notice_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='author',
            field=models.ForeignKey(default=notice.models.default_author, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notice',
            name='created',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='notice',
            name='updated',
            field=models.DateTimeField(),
        ),
    ]
