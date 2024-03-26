from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Book


# Create your views here.
class BooksList (ListView) :
    model = Book
    fields = '__all__'

class BooksDetail (DetailView) :
    model = Book
    fields = '__all__'


class AddBook (CreateView) :
    model = Book
    fields = '__all__'
    success_url = '/books'


class EditBook (UpdateView) :
    model = Book
    fields = '__all__'
    template_name = 'library/book_edit.html'
    success_url = '/books'

class DeleteBook (DeleteView):
    model = Book
    # template_name = 'library/book_confirm_delete.html'
    success_url = '/books'