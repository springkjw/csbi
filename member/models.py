from __future__ import unicode_literals

from django.db import models


def image_location(instance, filename):
    return "member/%s/%s" % (instance, filename)


TYPE_CHOICES = (
    ('Professor', 'Professor'),
    ('Research Professor', 'Research Professor'),
    ('Post Doctoral Fellow', 'Post Doctoral Fellow'),
    ('Ph.D. Candidate', 'Ph.D. Candidate'),
    ('Master Candidate', 'Master Candidate'),
    ('Staff', 'Staff'),
    ('Alumni', 'Alumni'),
)


class Member(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=image_location
    )
    phd = models.CharField(max_length=120, null=True, blank=True)
    ms = models.CharField(max_length=120, null=True, blank=True)
    bs = models.CharField(max_length=120, null=True, blank=True)
    field = models.CharField(max_length=255, null=True, blank=True)
    project = models.TextField(null=True, blank=True)
    homepage = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    graduation = models.CharField(max_length=20, null=True, blank=True)
    type = models.CharField(max_length=120, choices=TYPE_CHOICES, default='Master Candidate')
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)


    def __unicode__(self):
        return self.name

    @property
    def get_shorcut(self):
        if self.field:
            return self.field
        else:
            return self.type

    @property
    def get_image_url(self):
        if self.image:
            return "/media/%s" % (self.image)
        else:
            return "/static/img/no-profile.jpg"