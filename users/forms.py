from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    """
    Form used to register new users.

    Extends Django's built-in UserCreationForm by adding
    an email field.
    """

    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class ProfileUpdateForm(ModelForm):
    """
    Form used to update profile information.
    """

    class Meta:
        model = Profile

        fields = [
            "role",
            "phone_number",
            "address",
            "bio"
        ]