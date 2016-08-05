from __future__ import unicode_literals
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('accounts.User')
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
