from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProfileUpdateForm
from .forms import UserRegisterForm


def register(request):
    """
    Display and process the user registration form.
    """

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")

            messages.success(
                request,
                f"Account created for {username}. You can now log in."
            )

            return redirect("login")
    else:
        form = UserRegisterForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def profile(request):
    """
    Display and update profile.
    """

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            instance=request.user.profile
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Profile updated successfully."
            )

            return redirect("profile")

    else:

        form = ProfileUpdateForm(
            instance=request.user.profile
        )

    return render(
        request,
        "users/profile.html",
        {"form": form}
    )