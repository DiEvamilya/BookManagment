from django import forms

from BookManagmentapp.models import Book, Author


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = 'title', 'author', 'year_of_publication', 'genres', 'rating'
        exclude = ['slug']

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
