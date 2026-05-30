from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from projects.models import Project


def home(request):
    return render(request, "core/home.html")


@login_required
def dashboard(request):
    projects = Project.objects.filter(owner=request.user)

    context = {
        "total_projects": projects.count(),
        "planning_projects": projects.filter(status="planning").count(),
        "in_progress_projects": projects.filter(status="in_progress").count(),
        "completed_projects": projects.filter(status="completed").count(),
        "recent_projects": projects[:5],
    }

    return render(request, "core/dashboard.html", context)
