# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

PROTOCOL_TYPE = (
    ('journal', 'Journal Club'),
    ('paper', 'Paper Presentation'),
    ('protocol', 'Protocols'),
    ('lecture', '지식재산대학원특강'),
)

class Protocol(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=50, default='journal')
    presenter = models.CharField(max_length=10, null=True, blank=True)

    def __unicode__(self):
        return self.title