from __future__ import unicode_literals

from django.db import models
from django_summernote import fields as summer_fields
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class NoticeQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)


class NoticeManager(models.Manager):
    def get_queryset(self):
        return NoticeQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()


TYPE_CHOICES = (
    ('notice', 'notice'),
    ('news', 'news'),
)


class Notice(models.Model):
    title = models.CharField(max_length=120)
    type = models.CharField(max_length=120, choices=TYPE_CHOICES, default='notice')
    content = summer_fields.SummernoteTextField(null=True, blank=True)
    author = models.ForeignKey(User)
    active = models.BooleanField(default=True)
    like = models.PositiveIntegerField(default=0)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    objects = NoticeManager()

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-created", "-updated"]

    @property
    def get_absolute_url(self):
        return reverse('notice_detail', kwargs={"notice_id": self.id})
