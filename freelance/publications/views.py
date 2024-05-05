from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required

from .forms import ProjectForm
from .models import Project

from users.models import User

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

def publication_close(request, id):
    project = Project.objects.get(id=id)
    project.status = Project.STATUS_CHOICES[2][0]
    project.save()

    application = Application.objects.get(project_id=project.id, status=Application.STATUS_CHOICES[1][0])
    application.status = Application.STATUS_CHOICES[3][0]
    application.save()

    executor = User.objects.get(id=application.executor.id)

    executor.successful_projects = int(executor.successful_projects) + 1
    executor.save()
    try:
        new_rating = int(request.POST['rating'])
        current_rating = executor.rating
        num_of_projects = executor.successful_projects
        rating = (new_rating+current_rating)/num_of_projects
        executor.rating = rating
        executor.save()
    except ValueError:
        return redirect('publications:publication', id=id)
    return redirect('publications:publication', id=id)
