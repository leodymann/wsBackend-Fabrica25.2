# books/urls.py

from django.urls import path
from .views import BookListCreateAPIView, BookRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('<int:pk>/', BookRetrieveUpdateDestroyAPIView.as_view(), name='book-detail'),
]
