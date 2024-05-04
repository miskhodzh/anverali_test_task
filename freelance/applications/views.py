from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required

from .forms import ApplicationForm
from .models import Application
from publications.models import Project
from users.models import User

@permission_required(perm='applications.add_application', raise_exception=True)
def create_application(request, id):
    if request.method == 'POST':
        application = Application(
            project=Project.objects.get(id=id),
            executor=request.user
        )
        if Application.objects.filter(project=Project.objects.get(id=id), executor=request.user):
            print('Вы уже оставили заявку')
            return redirect('publications:publication', id=id)
        else:
            application.save()

    return redirect('publications:publication', id=id)

def applications_list(request):
    template = 'publications/main.html'
    return render(request, template)

def approve_func(request, id):
    # Можно сделать лучше
    application = Application.objects.get(id=id)
    for un_app_application in Application.objects.filter(project_id=application.project_id):
        un_app_application.status = Application.STATUS_CHOICES[2][0]
        print('Отклон')
        un_app_application.save()

    application.status = Application.STATUS_CHOICES[1][0]
    application.save()

    return redirect('publications:publication', id=application.project_id)
