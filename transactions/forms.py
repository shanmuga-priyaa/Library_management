from django import forms
from .models import *
class transactionForm(forms.ModelForm):
    class Meta:
        model = transaction
        fields = '__all__'