from rest_framework import serializers
from .models import Collection

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title', 'author', 'published_date', 'isbn', 'cover_image']
