from distutils.log import Log
from django.shortcuts import render
from .models import Book, Author, BookInstance, Language, Genre
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required(login_url='/accounts/login')
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

    # count the number of times someone has visited the homepage and store that information
    # in a session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'the_books': the_books,
        'num_genre': num_genre,
        'num_visits': num_visits
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)

class BookListView(LoginRequiredMixin, ListView):
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


class BookDetailView(LoginRequiredMixin, DetailView):
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

class AuthorListView(LoginRequiredMixin, ListView):
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
    paginate_by = 4 

class AuthorDetailView(LoginRequiredMixin, DetailView):
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

class LoanedBooksByUserListView(LoginRequiredMixin, ListView):
    """
    Generates a list of all books instances borrowed by the user. It extends Django's generic view ListView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        ListView (Generic View): Django's generic view for displaying a list of model
        objects.
        LoginRequiredMixin: Requires that the user is logged in before acessing the page view.
    
    Returns:
            Returns a list of all objects of the specified model. The list is rendered in 
            a HTML view.
    """ 
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'

    paginate_by = 10

    def get_queryset(self):
        """
            Get list of books on loan to user
        """
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')   


class AllBorrowedBooks(PermissionRequiredMixin, ListView):
    """
    Generates a list of all books instances borrowed by all users. It extends Django's generic view ListView 
    which does most of the work of retrieving the data and displaying using the appropriate 
    templates.

    Args:
        ListView (Generic View): Django's generic view for displaying a list of model
        objects.
        PermissionRequiredMixin: Requires that the user has permission before acessing the page view.
    
    Returns:
            Returns a list of all objects of the specified model. The list is rendered in 
            a HTML view.
    """ 
    model = BookInstance
    template_name = 'catalog/all_borrowed_books_list.html'
    permission_required = 'catalog.can_mark_returned'
    
    paginate_by = 10

    def get_queryset(self):
        """Gets a list all books instances that have been borrowed with the borrower
            field not null or empty.
        """
        return BookInstance.objects.exclude(borrower__isnull=True).order_by('borrower')
