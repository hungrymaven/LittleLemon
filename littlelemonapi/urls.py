# urls.py
from django.urls import path
from .views import BookListCreateAPIView, BookDetailAPIView

urlpatterns = [
    path('api/books', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('api/books/<int:pk>', BookDetailAPIView.as_view(), name='book-detail'),
    path('books', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>', BookDetailAPIView.as_view(), name='book-detail'),
]
