from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .forms import UserRegistrationForm
from .models import User

from publications.models import Project
from applications.models import Application

class CustomUserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    model = User

    def form_valid(self, form):
        user = form.save(commit=False)
        group_name = form.cleaned_data.get('group')
        group = Group.objects.get(name=group_name)
        user.save()
        user.groups.add(group)
        return super().form_valid(form)

@login_required
def profile(request):
    template = 'profile.html'
    user = request.user
    group = str(user.groups.first())

    context = {}
    if group == 'Customers':
        context['projects'] = Project.objects.filter(customer=user)
    elif group == 'Executors':
        applications = Application.objects.filter(executor=user)
        context['applications'] = applications

    return render(request, template, context)

def user_info(request, username):
    template = 'user_info.html'
    user = User.objects.get(username=username)
    return render(request, template, {'user':user})

def executors(request):
    template = 'users_list.html'
    executors_group = Group.objects.get(name='Executors')
    executors = executors_group.user_set.all()
    return render(request, template, {'executors': executors})
