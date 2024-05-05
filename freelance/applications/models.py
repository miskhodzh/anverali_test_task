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
        ('Successful', 'Успешно'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Pending'
    )
    def get_fields(self):
        return [
            self.id,
            self.project.title,
            self.executor,
            self.date_pub,
            self.status,
        ]
    @classmethod
    def get_verbose_names(cls):
        return [field.verbose_name for field in cls._meta.fields]
