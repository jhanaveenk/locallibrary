from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    num_genres = Genre.objects.all().count()

    num_book_available=Book.objects.filter(title__icontains='A').count()

    # a context variable, which is a Python dictionary, containing the data to insert into the placeholders in render function.
    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres' : num_genres,
        'num_book_available': num_book_available,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
