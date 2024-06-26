"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from library.views import BooksList, AddBook, BooksDetail, EditBook, DeleteBook

urlpatterns = [
    path('admin/', admin.site.urls),

    path('books/', BooksList.as_view()),
    path('books/add_book/', AddBook.as_view()),
    path('books/<int:pk>', BooksDetail.as_view()),
    path('books/<int:pk>/edit_book/', EditBook.as_view()),
    path('books/<int:pk>/delete_book/', DeleteBook.as_view()),


]
