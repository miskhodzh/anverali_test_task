from django.urls import path

from .views import admin_info, admin_get_object

app_name = 'admin_panel'

urlpatterns = [
    path('admin_info/', admin_info, name='admin_info'),
    path('admin_info/<str:object_type>/', admin_get_object, name='admin_get_objects'),
]
