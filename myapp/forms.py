from django import forms
from django.forms import ModelForm
from .models import ShortenUrl


class CreateForm(ModelForm):
    class Meta:
        model = ShortenUrl
        fields = ['original_url', 'url']

