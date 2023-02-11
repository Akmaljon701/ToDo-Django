from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Kundalik
        fields = '__all__'