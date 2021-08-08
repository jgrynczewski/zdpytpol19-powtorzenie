from django.shortcuts import render
from django.views.generic.list import ListView

from book.models import Book


class BookListView(ListView):
    model=Book
