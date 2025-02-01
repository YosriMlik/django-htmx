from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input block w-full mt-1 border-2 border-gray-300 rounded-md shadow-sm'}),
            'author': forms.TextInput(attrs={'class': 'form-input block w-full mt-1 border-2 border-gray-300 rounded-md shadow-sm'}),
            'published_date': forms.DateInput(attrs={'class': 'form-input block w-full mt-1 border-2 border-gray-300 rounded-md shadow-sm', 'type': 'date'}),
            'isbn': forms.TextInput(attrs={'class': 'form-input block w-full mt-1 border-2 border-gray-300 rounded-md shadow-sm'}),
        }
