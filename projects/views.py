from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Project

# Create your views here.


def index(request):
    projects = Project.objects.filter(visible=True)
    if request.user.has_perm('projects.view_hidden'):
        projects = Project.objects.all()

    return render(request, 'projects/index.html', {
        'projects': projects
    })


def project(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if not project.visible and not request.user.has_perm('projects.view_hidden'):
        raise Http404("Project not found")

    return render(request, 'projects/project.html', {
        'project': project
    })
