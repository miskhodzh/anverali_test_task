from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group


from .models import User

class UserRegistrationForm(UserCreationForm):

    group = forms.ChoiceField(choices=[(group.name, group.name) for group in Group.objects.all()])

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)