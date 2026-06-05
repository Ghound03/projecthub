from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from projects.models import Project


def home(request):
    return render(request, "core/home.html")


@login_required
def dashboard(request):

    projects = Project.objects.filter(
        owner=request.user
    )

    planning_count = projects.filter(
        status="planning"
    ).count()

    in_progress_count = projects.filter(
        status="in_progress"
    ).count()

    completed_count = projects.filter(
        status="completed"
    ).count()

    delayed_count = projects.filter(
        status="delayed"
    ).count()

    context = {
        "total_projects": projects.count(),
        "planning_projects": planning_count,
        "in_progress_projects": in_progress_count,
        "completed_projects": completed_count,
        "recent_projects": projects[:5],

        "chart_planning": planning_count,
        "chart_in_progress": in_progress_count,
        "chart_completed": completed_count,
        "chart_delayed": delayed_count,
    }

    return render(
        request,
        "core/dashboard.html",
        context
    )