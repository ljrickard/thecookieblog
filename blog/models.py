from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import uuid


class Post(models.Model):
    external_id = models.CharField(max_length=32, null=False, unique=True)
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    published_on = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def __init__(self):
        self.externalId = str(uuid.uuid4())

    def publish(self):
        self.publishedOn = timezone.now()
        self.save()
