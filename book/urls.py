from django.urls import path

from book import views

app_name = 'book'

urlpatterns = [
    path('list/', views.BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='book-detail')
]