from .models import Author, Book, Genre
from django import forms


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres']
        widgets = {
            'genres' : forms.CheckboxSelectMultiple()
        }