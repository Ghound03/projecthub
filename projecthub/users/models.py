from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    """
    Additional information linked to a Django user.
    """

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True
    )

    address = models.CharField(
        max_length=255,
        blank=True
    )

    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.user.username} Profile"