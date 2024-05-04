from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required

from .forms import ProjectForm
from .models import Project

from applications.forms import ApplicationForm
from applications.models import Application

@permission_required(perm='publications.add_project', raise_exception=True)
def create_project(request):
    template = 'publications/form.html'
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.customer = request.user
            project.save()
            return redirect('users:profile')
    else:
        form = ProjectForm()
    
    context = {
        'form': form,
    }

    return render(request, template, context)

@permission_required(perm='publications.change_project', raise_exception=True)
def publication_edit(request, id):
    template_name = 'publications/form.html'
    model = Project
    object = get_object_or_404(model, id=id)
    
    if request.method == 'POST':
        form = ProjectForm(data = request.POST, instance=object)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = ProjectForm(instance=object)

    context = {
        'form': form,
    }

    return render(request, template_name, context)

@permission_required(perm='publications.delete_project', raise_exception=True)
def publication_delete(request, id):
    template_name = 'publications/confirm_delete.html'
    model = Project
    object = get_object_or_404(model, id=id)

    if request.method == 'POST':
        object.delete()
        return redirect('users:profile')

    context = {
        'project': object,
    }    

    return render(request, template_name, context)

@login_required
def publications(request):
    template = 'publications/main.html'
    projects = Project.objects.order_by('-id')
    context = {
        'projects': projects,
    }
    return render(request, template, context)

def publication(request, id):
    template = 'publications/project.html'
    project = Project.objects.get(id=id)
    applications = Application.objects.filter(project=project)
    context = {
        'project': project,
        'applications': applications
    }
    return render(request, template, context)
