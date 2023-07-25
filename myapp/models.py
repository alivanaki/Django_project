from django.db import models

class ShortenUrl(models.Model):

    url = models.CharField(max_length=200, unique=True)
    original_url = models.URLField(max_length=200)
    counter = models.IntegerField(default=0)

    def __str__(self):
        return self.url