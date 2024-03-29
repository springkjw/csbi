# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Research',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=1)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Vision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
