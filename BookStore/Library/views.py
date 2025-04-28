from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Book, Genre
from .forms import AuthorForm, BookForm, GenreForm

# Create your views here.
def addauthor(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'addauthor.html', {'form': form})

def addbooks(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'addbooks.html', {'form': form})

def authors(request):
    author = Author.objects.all()
    return render(request, 'authors.html', {'author' : author})

def books(request):
    book = Book.objects.select_related('author').all()
    return render(request, 'books.html', {'book' : book})

def deleteAuthor(request, pk):
    author = get_object_or_404(Author, pk =pk)
    author.delete()
    return redirect('authors')

def addgenre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addgenre')
    else:
        form = GenreForm()
    return render(request, 'addgenre.html', {'form' : form})

def genres(request):
    genre = Genre.objects.all()
    return render(request, 'genres.html', {'genre' : genre})

def deleteGenre(request, pk):
    genre = get_object_or_404(Genre, pk = pk)
    genre.delete()
    return redirect('genres')

def update(request, pk):
    book = get_object_or_404(Book, pk = pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)
    return render(request, 'updatebooks.html', {'form' : form})

def deletebook(request, pk):
    books = get_object_or_404(Book, pk = pk)
    books.delete()
    return redirect('books')