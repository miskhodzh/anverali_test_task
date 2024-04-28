from django.urls import path
from .views import publications, create_project

app_name = 'publications'

urlpatterns = [
    path('', publications, name='index'),
    path('add/', create_project, name='add'),
]
