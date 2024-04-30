from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import UserRegistrationForm
from django.urls import reverse_lazy
from .models import User

class CustomUserCreateView(CreateView):
    template_name = 'registration/registration_form.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    model = User

    def form_valid(self, form):
        # Получаем объект пользователя, созданный из формы
        user = form.save(commit=False)
        # Получаем имя выбранной группы из формы
        group_name = form.cleaned_data.get('group')
        # Находим объект группы по имени
        group = Group.objects.get(name=group_name)
        # Сохраняем пользователя
        user.save()
        # Присваиваем пользователю группу
        user.groups.add(group)
        return super().form_valid(form)

@login_required
def profile(request):
    template = 'profile.html'
    user = request.user
    # groups = user.groups.filter(name='Customers').exists()
    context = {
        'user': user,
    }
    return render(request, template, context)

def executors(request):
    template = 'users_list.html'
    return render(request, template)
