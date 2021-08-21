from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


from book.models import Book


class BookListView(ListView):
    model=Book


class BookDetailView(DetailView):
    model = Book


class BookCreateView(CreateView):
    model = Book
    fields = [
        'title',
        'category',
        'price'
    ]

class BookUpdateView(UpdateView):
    model = Book
    fields = [
        'title',
        'category',
        'price'
    ]
    template_name_suffix = "_update"
