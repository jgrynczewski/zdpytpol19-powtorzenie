from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from book.models import Book


class BookListView(ListView):
    model=Book


class BookDetailView(DetailView):
    model = Book

