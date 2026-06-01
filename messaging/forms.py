from django import forms
from django.contrib.auth.models import User

from .models import Message


class MessageForm(forms.ModelForm):
    """
    Form used to send messages between users.
    """

    receiver = forms.ModelChoiceField(
        queryset=User.objects.all(),
        empty_label="Select a user"
    )

    class Meta:
        model = Message

        fields = [
            "receiver",
            "subject",
            "body",
        ]

        widgets = {
            "body": forms.Textarea(attrs={"rows": 5}),
        }