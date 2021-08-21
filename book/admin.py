from django.contrib import admin

from book.models import Book
from book.models import Person
from book.models import Loan

# Register your models here.
admin.site.register(Book)
admin.site.register(Person)
admin.site.register(Loan)
