from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('publications.urls'), name='publications'),
    path('auth/', include('users.urls'), name='users'),
    path('application/', include('applications.urls'), name='applications'),
    path('admin/', admin.site.urls),
]
