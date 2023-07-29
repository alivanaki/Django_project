from django.shortcuts import get_object_or_404
from Shorten_URL.models import ShortenUrl
from django.shortcuts import redirect
from django.views import View


class RedirectView(View):
    def get(self, *args, **kwargs):

        shorten_url = get_object_or_404(ShortenUrl, url=kwargs['shorten_url'])
        shorten_url.counter += 1
        shorten_url.save()
        return redirect(shorten_url.original_url)

