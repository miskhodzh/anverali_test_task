from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView

from django.contrib.auth import views
from django.urls import path, reverse_lazy

from .views import profile

app_name = 'users'

urlpatterns = [
    # Логин.
    path(
        'login/',
        views.LoginView.as_view(),
        name='login'
    ), 
    # Логаут.
    path(
        'logout/',
        views.LogoutView.as_view(next_page=reverse_lazy('users:login')),
        name='logout'
    ),

    # Изменение пароля.
    path(
        'password_change/',
        views.PasswordChangeView.as_view(),
        name='password_change'
    ),
    # Сообщение об успешном изменении пароля.
    path(
        'password_change/done/',
        views.PasswordChangeDoneView.as_view(),
        name='password_change_done'
    ),

    # Восстановление пароля.
    path(
        'password_reset/',
        views.PasswordResetView.as_view(
            success_url=reverse_lazy('users:password_reset_done'),
        ),
        name='password_reset'
    ),
    # Сообщение об отправке ссылки для восстановления пароля.
    path(
        'password_reset/done/',
        views.PasswordResetDoneView.as_view(),
        name='password_reset_done'
    ),
    # Вход по ссылке для восстановления пароля.
    path(
        'reset/<uidb64>/<token>/',
        views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'
    ),
    # Сообщение об успешном восстановлении пароля.
    path(
        'reset/done/',
        views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'
    ),

    # Регистрация
    path(
        'registration/', 
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('users:login'),
        ),
        name='registration',
    ),

    # Профиль 
    path(
        'profile/',
        profile,
        name='profile'
    ),
] 