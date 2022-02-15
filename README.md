# Local Library
<img src="https://images.pexels.com/photos/1319854/pexels-photo-1319854.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940" height="500" width="1200">

***Photo by mentatdgt from Pexels***

Website: https://thawing-hamlet-88015.herokuapp.com/catalog/authors/

## Introduction
The Local Library is an online representation of a physical local library that allows users to borrow and return books, view the number of books that are available, check out the details about the book, etc.

## Installations
This application was built using Django. You can read more about Django and its installation [here.](https://www.djangoproject.com/) Since Django is a python web development framework, it requires python. Other required django libraries are included in the ***requirements.txt*** file in the project.

## Description
The entire Local library was developed using Django. The Local library is an online platform that helps manage a local physical library. Users can log in, view the total number of books in the library and browse through the collection. They will be able to borbrow a book on the website. During development, the backend database that was used was SQlite3. However, during deployment, since Heroku does not support sqlite3, the database was migrated to PostgreSQL. There is also an authors list which shows the list of all the authors in the database. For each author, you can view all the books the person has authored. This feature allows users to view all books written by their favourite author.

