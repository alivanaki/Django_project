from django import forms
from django.forms import ModelForm
from .models import ShortenUrl


class CreateForm(ModelForm):
    enctype = "multipart/form-data"
    class Meta:
        model = ShortenUrl
        fields = ['original_url', 'url', 'logo']

