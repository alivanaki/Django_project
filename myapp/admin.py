from django.contrib import admin
from .models import OriginalUrl, ShortenUrl

admin.site.register(OriginalUrl)
admin.site.register(ShortenUrl)
