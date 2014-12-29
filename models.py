from django.db import models

from datetime import datetime


class ShortUrl(models.Model):
    word = models.CharField(max_length=64, unique=True)
    url = models.URLField(max_length=256, unique=True, blank=True, null=True)
    changed_at_date_time = models.DateTimeField(auto_now=True, default=datetime.now())

    class Meta:
        ordering = ['-changed_at_date_time']

    def __str__(self):
        return self.word