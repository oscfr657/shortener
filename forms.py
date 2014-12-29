from django import forms

from .models import ShortUrl


class UrlForm(forms.ModelForm):

    url = forms.URLField(label="Url", help_text="Enter the url you want to shorten.")

    class Meta:
        model = ShortUrl
        exclude = ('word',)