from django.urls import path
from .views import publications, create_project, publication, publication_edit, publication_delete, publication_close

app_name = 'publications'

urlpatterns = [
    path('', publications, name='index'),
    path('add/', create_project, name='add'),
    path('publication/<int:id>/', publication, name='publication'),
    path('publication/edit/<int:id>/', publication_edit, name='publication_edit'),
    path('publication/delete/<int:id>/', publication_delete, name='publication_delete'),
    path('publication/close/<int:id>/', publication_close, name='publication_close'),
]
