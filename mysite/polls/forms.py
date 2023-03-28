from cProfile import label
import imp
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.forms import ModelForm
from .models import Question
from django import forms

class CreateNewList(forms.Form):
    name= forms.CharField(label="name", max_length="24")
    check= forms.BooleanField()