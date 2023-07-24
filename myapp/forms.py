from django import forms


class CreateForm(forms.Form):
    main_url = forms.URLField(label='main url', max_length=200)
    shorten_url = forms.CharField(label='shorten name', max_length=200)


class UpdateMainForm(forms.Form):
    url = forms.URLField(label='main url', max_length=200)


class UpdateShortenForm(forms.Form):
    url = forms.CharField(label='shorten url', max_length=200)