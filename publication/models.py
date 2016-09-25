from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from member.models import Member


class PublicationItem(models.Model):
    member = models.ForeignKey(Member)
    publication = models.ForeignKey('Publication')

    def __unicode__(self):
        return self.publication.title


TYPE_CHOICES = (
    ('journal', 'journal'),
    ('patents', 'patents'),
    ('conference', 'conference'),
    ('book', 'book'),
)


class Publication(models.Model):
    type = models.CharField(max_length=120, choices=TYPE_CHOICES, default='journal')
    author = models.TextField(null=True, blank=True)
    poeple = models.ManyToManyField(Member, through=PublicationItem)
    title = models.CharField(max_length=255, null=True, blank=True)
    journal = models.CharField(max_length=120, null=True, blank=True)
    patent = models.CharField(max_length=120, null=True, blank=True)
    conference = models.CharField(max_length=120, null=True, blank=True)
    book = models.CharField(max_length=120, null=True, blank=True)
    year = models.CharField(max_length=20, null=True, blank=True)
    content = models.CharField(max_length=255, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.title

    @property
    def get_absolute_url(self):
        return reverse('pub_detail', kwargs={"pub_id": self.id})