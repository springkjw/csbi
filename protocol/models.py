# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from member.models import Member


class ProtocolPresenter(models.Model):
    presenter = models.ForeignKey(Member)
    protocol = models.ForeignKey("Protocol")

    def __unicode__(self):
        return self.presenter.name


PROTOCOL_TYPE = (
    ('journal', 'Journal Club'),
    ('paper', 'Paper Presentation'),
    ('protocol', 'Protocols'),
    ('lecture', '지식재산대학원특강'),
)


def image_location(instance, filename):
    return "protocol/image/%s%s" % (instance, filename)

def video_location(instance, filename):
    pass


class Protocol(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=50, choices=PROTOCOL_TYPE, default='journal')
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=image_location
    )
    video = models.URLField(null=True, blank=True)
    paper_link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.title

    @property
    def get_image_url(self):
        if self.image:
            return "/media/%s" % (self.video)
        else:
            return "/static/img/no-video.png"

    @property
    def get_presenter(self):
        p_instance = Protocol.objects.get(id=self.id)
        p = ProtocolPresenter.objects.filter(protocol=p_instance)

        presenter = ''
        for item in p:
            presenter += str(item)

        return presenter