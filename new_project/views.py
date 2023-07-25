from django.shortcuts import get_object_or_404
from myapp.models import ShortenUrl
from django.shortcuts import redirect


def redirectview(request, shorten_url):

    shorten_url = get_object_or_404(ShortenUrl, url=shorten_url)
    shorten_url.counter += 1
    shorten_url.save()
    return redirect(shorten_url.original_url.url)