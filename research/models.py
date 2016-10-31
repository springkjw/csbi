from __future__ import unicode_literals

from django.db import models
from django_summernote import fields as summer_fields


class Vision(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    content = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.title


class Research(models.Model):
    title = models.CharField(max_length=120, null=False, blank=False)
    content = summer_fields.SummernoteTextField(null=True, blank=True)
    order = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order', ]
