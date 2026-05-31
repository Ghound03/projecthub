from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    """
    Categories used to organize projects.
    """

    name = models.CharField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Stores details about a project created by a user.
    """

    STATUS_CHOICES = [
        ("planning", "Planning"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
        ("delayed", "Delayed"),
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owned_projects"
    )

    category = models.ForeignKey(
    Category,
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name="projects"
     )

    name = models.CharField(
        max_length=100
    )

    description = models.TextField()

    start_date = models.DateField()

    end_date = models.DateField()

    stakeholders = models.TextField(
        help_text="List stakeholders involved in the project."
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="planning"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name