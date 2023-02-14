from django import forms
from .models import *

class AddForm(forms.ModelForm):
    class Meta:
        model = Kundalik
        fields = ('sarlavha', 'vaqt', 'malumot', 'holat')