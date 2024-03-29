# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields
import notice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('type', models.CharField(choices=[('notice', 'notice'), ('news', 'news')], default='notice', max_length=120)),
                ('content', django_summernote.fields.SummernoteTextField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('like', models.PositiveIntegerField(default=0)),
                ('updated', models.DateTimeField()),
                ('created', models.DateTimeField()),
                ('author', models.ForeignKey(default=notice.models.default_author, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created', '-updated'],
            },
        ),
    ]
