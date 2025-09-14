from django.urls import path
from .views import (
    BookSearchAPIView,
    CollectionListAPIView,
    CollectionAddAPIView,
    CollectionRemoveAPIView
)

urlpatterns = [
    path('search/', BookSearchAPIView.as_view(), name='book-search'),
    path('collections/', CollectionListAPIView.as_view(), name='collection-list'),
    path('collections/add/', CollectionAddAPIView.as_view(), name='collection-add'),
    path('collections/<int:pk>/remove/', CollectionRemoveAPIView.as_view(), name='collection-remove'),
]
