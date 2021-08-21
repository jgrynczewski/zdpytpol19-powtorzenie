from django.urls import path

from book import views

app_name = 'book'

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('bye/', views.bye, name='bye'),
    path('list/', views.BookListView.as_view(), name='book-list'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('create/', views.BookCreateView.as_view(), name='book-create'),
    path('update/<int:pk>', views.BookUpdateView.as_view(), name='book-update'),
    path('delete/<int:pk>', views.BookDeleteView.as_view(), name='book-delete'),
]