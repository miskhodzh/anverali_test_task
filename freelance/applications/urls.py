from django.urls import path
from .views import create_application, approve_func

app_name = 'applications'

urlpatterns = [
    path('add/<int:id>/', create_application, name='add'),
    path('application/approve/<int:id>/', approve_func, name='approve'),
]
