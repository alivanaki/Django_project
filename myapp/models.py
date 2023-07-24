from django.db import models


class OriginalUrl(models.Model):

    url = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.url


class ShortenUrl(models.Model):

    url = models.CharField(max_length=200, unique=True)
    original_url = models.ForeignKey(OriginalUrl, on_delete=models.CASCADE, related_name= 'shorten_urls')

    def __str__(self):
        return self.url