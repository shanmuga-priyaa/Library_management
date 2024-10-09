from django import forms
from .models import *
class memberForm(forms.ModelForm):
    class Meta:
        model = member
        fields = '__all__'