from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class ShortenUrl(models.Model):

    url = models.CharField('Shorten url', max_length=200, unique=True)
    original_url = models.URLField(max_length=200)
    counter = models.IntegerField(default=0)
    create_date = models.DateField(auto_now_add=True)
    last_edit_date = models.DateTimeField(auto_now=True)
    logo = models.ImageField(upload_to='Shorten_URL_app/', blank=True)

    def __str__(self):
        return self.url

    def clean(self, *args, **kwargs):

        if self.url == 'app' or self.url == 'admin':
            raise ValidationError({'url': "Reserved words"})
        super().clean(*args, **kwargs)