from django.db import models
from publications.models import Project
from users.models import User

class Application(models.Model):
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE
    )
    executor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    date_pub = models.DateField(
        auto_now_add=True
    )
    STATUS_CHOICES = [
        ('Pending', 'В ожидании'),
        ('Accepted', 'Принято'),
        ('Rejected', 'Отклонено'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )
