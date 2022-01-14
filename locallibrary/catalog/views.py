from django.shortcuts import render
from .models import Book, Author, BookInstance, Language, Genre

def index(request):
    """
    This is a view for the home page of the catalog app. It renders all the information
    that is displayed on the home page. 

    Args:
        request (HTTP):

    Returns:
        html that is displayed to the end-user.
    """    
    # get the count of most of the items
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

