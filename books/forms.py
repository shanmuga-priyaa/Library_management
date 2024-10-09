from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    AVAILABLE_CHOICES = [
        (True, 'Yes'), 
        (False, 'No'),  
    ]
    Available = forms.ChoiceField(choices=AVAILABLE_CHOICES, widget=forms.Select())

    class Meta:
        model = Book
        fields = ['Title', 'Author', 'ISBN', 'Publisher', 'Page_count', 'Available']
