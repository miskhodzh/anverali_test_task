from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator


class User(AbstractUser):

    profile_photo = models.ImageField(
        upload_to='static/img/profile_photos/',
        null=True,
        blank=True
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        default=0.0,
        max_length=2,
    )
    successful_projects = models.PositiveIntegerField(
        null=True,
        blank=True,
        default=0,
        validators=[MaxValueValidator(1_000_000)],
    )
    def get_fields(self):
        return [
            self.id,
            self.username,
            self.rating,
            self.successful_projects,
        ]

    def get_verbose_names():
        return [
            'id',
            'Имя пользователя',
            'Рейтинг',
            'Выполненные сделки',
        ]
