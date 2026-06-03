from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from users.permissions import is_admin
from .forms import ProjectForm
from .models import Project, Category


@login_required
def project_list(request):
    """
    Display projects with search and filtering.
    """

    projects = Project.objects.filter(
        owner=request.user
    )

    search_query = request.GET.get(
        "search",
        ""
    )

    status_filter = request.GET.get(
        "status",
        ""
    )

    category_filter = request.GET.get(
        "category",
        ""
    )

    if search_query:
        projects = projects.filter(
            name__icontains=search_query
        )

    if status_filter:
        projects = projects.filter(
            status=status_filter
        )

    if category_filter:
        projects = projects.filter(
            category_id=category_filter
        )

    categories = Category.objects.all()

    context = {
        "projects": projects,
        "categories": categories,
        "search_query": search_query,
        "status_filter": status_filter,
        "category_filter": category_filter,
    }

    return render(
        request,
        "projects/project_list.html",
        context
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
    if not is_admin(request.user):

     messages.error(
        request,
        "Only administrators can delete projects."
    )

     return redirect(
        "project_detail",
        pk=pk
    )

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