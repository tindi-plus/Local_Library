from django.contrib import admin
from .models import BookInstance, Book, Language, Genre, Author

# Register your models here.

# class BooksInline is used to enable Authors to be displayed with the
# number of their books instances. It is used with the inline word
class BooksInline(admin.TabularInline):
    model = Book

    # the extra feature shows the number of arbitrary new books object that are included
    # in the list of books inline waiting to be filled with information. This is set to 0
    # because we do not want any default books showing for an author. If a book is to be added
    # it should be done via 'Add Book'.
    extra = 0


# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """
    A class That allows the configuration of the admin properties for the Author Model

    Args:
        admin.ModelAdmin
    """   
    # for viewing a list of Author objects. list_display will display the lists
    # of fields as listed in the tuple. 
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')

    # for viewing the full details of an author object. Only the fields in the list 
    # will be displayed. List are usually displayed vertically. Putting them in a tuple
    # forces them to be displayed horizontally.
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

    # for showing the number of books each author has written. inlines does a count 
    # of the number of books each author has written.
    inlines = [BooksInline]

# now register the Author model with the associated Class model just created.
admin.site.register(Author, AuthorAdmin)


# class BookInstanceInline is used to enable Books to be displayed with the
# number of their books instances. It is used with the inline word
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    A class That allows the configuration of the admin properties for the Book Model

    Args:
        admin.ModelAdmin
    """    
    list_display = ('title', 'author', 'display_genre')

    inlines = [BooksInstanceInline]

admin.site.register(Book, BookAdmin)

#admin.site.register(BookInstance)
# Now create and register a model admin class using a decorator. Just another
# way of doing it.
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """
    A class That allows the configuration of the admin properties for the BookInstance Model

    Args:
        admin.ModelAdmin
    """    
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )


admin.site.register(Language)
admin.site.register(Genre)

