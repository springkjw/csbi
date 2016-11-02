# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 00:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='type',
            field=models.CharField(choices=[('Professor', 'Professor'), ('Research Professor', 'Research Professor'), ('Post Doctoral Fellow', 'Post Doctoral Fellow'), ('Ph.D. Candidate', 'Ph.D. Candidate'), ('Master Candidate', 'Master Candidate'), ('Staff', 'Staff'), ('Alumni', 'Alumni')], default='Master Candidate', max_length=120),
        ),
    ]
