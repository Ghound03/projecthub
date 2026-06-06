from django import forms

from .models import (Project, ProjectDocument)


class ProjectForm(forms.ModelForm):
    

    class Meta:
        model = Project

        fields = [
            "category",
            "name",
            "description",
            "start_date",
            "end_date",
            "stakeholders",
            "status",
        ]

        widgets = {
            "start_date": forms.DateInput(attrs={"type": "date"}),
            "end_date": forms.DateInput(attrs={"type": "date"}),
            "description": forms.Textarea(attrs={"rows": 4}),
            "stakeholders": forms.Textarea(attrs={"rows": 3}),
        }


class ProjectDocumentForm(forms.ModelForm):

    class Meta:
        model = ProjectDocument

        fields = [
            "title",
            "file",
        ]