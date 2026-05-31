from django.contrib import admin
from .models import Project, Category


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "owner",
        "status",
        "start_date",
        "end_date",
        "created_at",
    )

    list_filter = (
        "status",
        "start_date",
        "end_date",
    )

    search_fields = (
        "name",
        "description",
        "stakeholders",
    )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
    )

    search_fields = (
        "name",
    )