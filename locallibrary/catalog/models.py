# -*- coding: utf-8 -*-
"""
@create date: 10-01-2022 18:05:31
@modify date: 10-01-2022 18:05:31
@author: Tindi Sommers
@email: tindisommers@gmail.com
@desc: [description]
"""

from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date

# Create your models here.

class Language(models.Model):
    """
    A model of a language a book is written in. It has a name and a universal code.

    Args:
        models.Model
    """    

    name = models.CharField(max_length=50, help_text='Enter the full name of the language in English')
    code = models.CharField(max_length=2, null=True, blank=True, 
                            help_text='Enter the universal language code for the language (eg es for Spanish)')
    
    def __str__(self) -> str:
        """
        Returns:
            str: Return a string representation of the genre object
        """        
        return f'Name: {self.name}; Code: {self.code}'


class Genre(models.Model):
    """ 
    Model representing a book genre

    Args:
        models (Model): [description]
    """  

    name = models.CharField(max_length=200, help_text='Enter a book genre eg Science Fiction')  

    def __str__(self) -> str:
        """
        Returns:
            str: Return a string representation of the genre object
        """        
        return self.name


class Book(models.Model):
    """
    Model representing a book in a general sense

    Args:
        models (Model): [description]
    """ 
    title = models.CharField(max_length=200)

    # foreign key used to link the book model to the author model. This is a
    # one to many relationship. A book has only 1 author but an author can have multiple books.
    
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book.")
    isbn = models.CharField('ISBN', max_length=13, 
    help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    # a genre of the book. But a book has a many to many relationship with a genre. 
    genre = models.ManyToManyField(Genre, help_text='Select a genre for the book')

    # a language a book is written in. Book has a one to many relationship with Language. 
    # A book can only have on language, while many books can be written in one language.
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True,
                                    help_text='Select the language the book is written in')

    def __str__(self) -> str:
        """
        Returns:
            str: Representation of the model object
        """        
        return self.title

    def get_absolute_url(self):
        """
        Returns:
            url: a url for accessing details about this book object
        """        
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        """
        Create a string for the Genre. This is required to display genre in Admin.

        Returns:
            str: The names of the first 3 genres in the book object if they exist
        """    
        return ', '.join([genre.name for genre in self.genre.all()[:3]])    

    display_genre.short_description = 'Genre'

    class meta:
        ordering = ['title']



import uuid # Required for unique book instances
class BookInstance(models.Model):
    """
    Model representing a specific copy of a book
    Args: None
    """    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, 
    help_text='Unique ID for this particular book across whole library' )

    book = models.ForeignKey(Book, on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    # A user who is a borrower of a book instance
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(
        max_length=1,
        choices=LOAN_STATUS,
        default='m',
        blank=True,
        help_text='Book Availability' 
    )

    @property
    def is_overdue(self):
        "Check if a book is overdue to be returned"
        if self.due_back and date.today() > self.due_back:
            return True
        return False
    

    class Meta:
        ordering = ['due_back']
        permissions = (("can_mark_returned", "Set book as returned"),)
    
    def __str__(self) -> str:
        """
        Returns:
            str: Representation of the model object
        """        
        return f'{self.id} ({self.book.title})'
    

class Author(models.Model):
    """
    A model representing an author of a book.

    Args:
        models.Model
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)

    class meta:
        ordering = ['last_name', 'first_name']  

    def get_absolute_url(self):
        """
        Returns:
            url : an absolute url for accessing a particular author's details. The url is reversed
                  by a url mapper that is defined and named in urls.py
        """        
        return reverse('author-detail', args=[str(self.id)])  


    def __str__(self) -> str:
        """
        Returns:
            str: Representation of the model object
        """        
        return f'{self.last_name}, {self.first_name}'