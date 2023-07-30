from rest_framework import serializers
from .models import ShortenUrl


class ShortenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortenUrl
        fields = ['id', 'url', 'original_url', 'logo', 'create_date', 'last_edit_date', 'counter']
        read_only_fields = ['counter']
