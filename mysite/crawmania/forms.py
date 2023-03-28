from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from crawmania.models import PrizeWinners

class Nameform(forms.Form):
    user_name = forms.CharField(help_text="Enter your name")

    def clean_user_name(self):
        data= self.cleaned_data['user_name']
        return data

class prizeform(forms.Form):
    class Meta:
        model=PrizeWinners
        fields=['winner','text','year','prize','image']