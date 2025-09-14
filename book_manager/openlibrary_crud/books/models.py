# books/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    cover_url = models.URLField(max_length=500, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
