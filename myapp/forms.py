from django import forms
from django.forms import ModelForm
from .models import ShortenUrl


class CreateForm(ModelForm):
    class Meta:
        model = ShortenUrl
        fields = ['original_url', 'url']


class UpdateMainForm(forms.Form):
    url = forms.URLField(label='main url', max_length=200)


class UpdateShortenForm(forms.Form):
    url = forms.CharField(label='shorten url', max_length=200)