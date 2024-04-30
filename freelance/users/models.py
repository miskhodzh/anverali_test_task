from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    profile_photo = models.ImageField(
        upload_to='static/img/profile_photos/',
        null=True,
        blank=True
    )
