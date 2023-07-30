from rest_framework import viewsets
from .models import ShortenUrl
from .serializers import ShortenSerializer


class ShortenerView(viewsets.ModelViewSet):

    queryset = ShortenUrl.objects.all()
    serializer_class = ShortenSerializer
