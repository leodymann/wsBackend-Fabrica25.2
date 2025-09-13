from django.db import models
from django.contrib.auth.models import User

class Pokemon(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='team'
    )
    name = models.CharField(
        max_length=100
    )
    nickname = models.CharField(
        max_length=100,
        blank=True
    )
    pokeapi_id = models.IntegerField()
    image_url = models.URLField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.nickname or self.name} ({self.user.username})"