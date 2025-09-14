from rest_framework import serializers
from .models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    # Serializer to Model collection
    class Meta:
        model = Collection
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'cover_image'] # exposed values
