from django.shortcuts import render

from publications.models import Project
from applications.models import Application
from users.models import User

def admin_info(request):
    template = 'admin/admin_info.html'
    context = {
        'projects': Project.objects.all(),
        'applications': Application.objects.all(),
        'users': User.objects.all(),
    }
    return render(request, template, context)

def admin_get_object(request, object_type):
    template = 'admin/admin_info.html'
    objects = {
        'projects': Project,
        'applications': Application,
        'users': User,
    }
    print({'objects':objects[object_type]})
    return render(
        request,
        template,
        {
            'objects':objects[object_type].objects.all(),
            'headers':objects[object_type].get_verbose_names()
        }
    )
