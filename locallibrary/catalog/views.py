from django.shortcuts import render
from .models import Book, Author, BookInstance, Language, Genre
from django.views.generic import ListView, DetailView

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
    num_genre = Genre.objects.all().count()

    # get all books with 'The' in the summary
    the_books = Book.objects.filter(summary__contains='The').count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'the_books': the_books,
        'num_genre': num_genre
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(ListView):
    """
    Generates a list all books in the database. It extends Django's generic view ListView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        ListView (Generic View): Django's generic view for displaying a list of model
        objects.
    
    Returns:
            Returns a list of all objects of the specified model. The list is rendered in 
            a HTML view.
    """    

    model = Book
    # paginate enables the list view to fetch a certain number of records per page. This is
    # useful when the records are plenty and it is not possible to display all in one page.
    paginate_by = 3 


class BookDetailView(DetailView):
    """
    Generates a detail view of books in the database. It extends Django's generic view DetailView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        DetailView (Generic View): Django's generic view for displaying the details of model
        objects.
    
    Returns:
            Returns the details of an object of the specified model. The list is rendered in 
            a HTML view.
    """    
    model = Book

class AuthorListView(ListView):
    """
    Generates a list all authors in the database. It extends Django's generic view ListView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        ListView (Generic View): Django's generic view for displaying a list of model
        objects.
    
    Returns:
            Returns a list of all objects of the specified model. The list is rendered in 
            a HTML view.
    """    
    model = Author

    # paginate enables the list view to fetch a certain number of records per page. This is
    # useful when the records are plenty and it is not possible to display all in one page.
    paginate_by = 3 

class AuthorDetailView(DetailView):
    """
    Generates a detail view of authors in the database. It extends Django's generic view DetailView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        DetailView (Generic View): Django's generic view for displaying the details of model
        objects.
    
    Returns:
            Returns the details of an object of the specified model. The list is rendered in 
            a HTML view.
    """    
    model = Author


