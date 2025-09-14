from django.urls import path
from .views import (
    BookSearchAPIView,
    CollectionListAPIView,
    CollectionAddAPIView,
    CollectionRemoveAPIView
)

urlpatterns = [
    path('search/', BookSearchAPIView.as_view(), name='book-search'), # search book
    path('collections/', CollectionListAPIView.as_view(), name='collection-list'), # list collection url
    path('collections/add/', CollectionAddAPIView.as_view(), name='collection-add'), # add book url
    path('collections/<int:pk>/remove/', CollectionRemoveAPIView.as_view(), name='collection-remove'), # delete book url
]
