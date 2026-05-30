from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectForm
from .models import Project


@login_required
def project_list(request):
    """
    Display all projects owned by the logged-in user.
    """

    projects = Project.objects.filter(owner=request.user)

    return render(
        request,
        "projects/project_list.html",
        {"projects": projects}
    )


@login_required
def project_detail(request, pk):
    """
    Display full information for one project.
    """

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user
    )

    return render(
        request,
        "projects/project_detail.html",
        {"project": project}
    )


@login_required
def project_create(request):
    """
    Create a new project for the logged-in user.
    """

    if request.method == "POST":
        form = ProjectForm(request.POST)

        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()

            messages.success(
                request,
                "Project created successfully."
            )

            return redirect("project_list")

    else:
        form = ProjectForm()

    return render(
        request,
        "projects/project_form.html",
        {"form": form, "title": "Create Project"}
    )


@login_required
def project_update(request, pk):
    """
    Update an existing project owned by the logged-in user.
    """

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        form = ProjectForm(
            request.POST,
            instance=project
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Project updated successfully."
            )

            return redirect("project_detail", pk=project.pk)

    else:
        form = ProjectForm(instance=project)

    return render(
        request,
        "projects/project_form.html",
        {"form": form, "title": "Update Project"}
    )


@login_required
def project_delete(request, pk):
    """
    Delete an existing project owned by the logged-in user.
    """

    project = get_object_or_404(
        Project,
        pk=pk,
        owner=request.user
    )

    if request.method == "POST":
        project.delete()

        messages.success(
            request,
            "Project deleted successfully."
        )

        return redirect("project_list")

    return render(
        request,
        "projects/project_confirm_delete.html",
        {"project": project}
    )