# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

PROTOCOL_TYPE = (
    ('journal', 'Journal Club'),
    ('paper', 'Paper Presentation'),
    ('protocol', 'Protocols'),
    ('lecture', '지식재산대학원특강'),
)


def image_location(instance, filename):
    return "video/%s/%s" % (instance, filename)


class Protocol(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=50, default='journal')
    presenter = models.CharField(max_length=10, null=True, blank=True)
    video = models.FileField(
        blank=True,
        null=True,
        upload_to=image_location
    )
    paper_link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    @property
    def get_video_url(self):
        return "/media/%s" % (self.video)
