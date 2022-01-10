from django.contrib import admin
from .models import BookInstance, Book, Language, Genre, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(Author)
admin.site.register(Language)
admin.site.register(Genre)

