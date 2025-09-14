from django.db import models
from django.conf import settings

class Collection(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='collections')
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255, blank=True)
    published_date = models.CharField(max_length=50, blank=True)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    cover_image = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.user.username}"
