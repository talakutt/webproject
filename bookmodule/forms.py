from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    title = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    author = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    price = forms.FloatField(min_value=0.0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    edition = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

