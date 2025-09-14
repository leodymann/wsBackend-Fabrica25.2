from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Collection
from .serializers import CollectionSerializer
from .utils import fetch_books_by_title

class BookSearchAPIView(APIView):
    # consuming the API
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        title = request.query_params.get('title')
        if not title:
            return Response({"error": "Title query param is required."}, status=400)
        results = fetch_books_by_title(title)
        return Response(results)

class CollectionListAPIView(generics.ListAPIView):
    # list collection user
    serializer_class = CollectionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Collection.objects.filter(user=self.request.user)

class CollectionAddAPIView(APIView):
    # add book in collection user
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class CollectionRemoveAPIView(APIView):
    # remove book in collection user
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        try:
            book = Collection.objects.get(pk=pk, user=request.user)
            book.delete()
            return Response(status=204)
        except Collection.DoesNotExist:
            return Response({"error": "Book not found in your collection."}, status=404)
