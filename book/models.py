from django.db import models
from django.shortcuts import reverse


CATEGORIES = [
    (1, "Comedy"),
    (2, "Thriller"),
    (3, "Romance"),
]


class Book(models.Model):
    added = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    category = models.IntegerField(choices=CATEGORIES)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book:book-list')


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Loan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='loans')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} przez {self.person}"