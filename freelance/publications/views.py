from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.models import User

from .forms import ProjectForm
from .models import Project


def create_project(request):
    template = 'publications/add.html'
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            # Создаем объект статьи, заполняем автора и сохраняем
            project = form.save(commit=False)
            project.customer = request.user
            project.save()
            return redirect('publications:index')  # Перенаправляем на страницу со списком статей
    else:
        form = ProjectForm()
    return render(request, template, {'form': form})


@login_required
def publications(request):
    template = 'publications/main.html'
    projects = Project.objects.order_by('-id')
    # for project in projects:
    #     project.user = User.objects.get(id=project.customer)
    context = {
        'projects': projects
    }
    return render(request, template, context)

def publication(request):
    template = 'publications/publication.html'
    return render(request, template)
