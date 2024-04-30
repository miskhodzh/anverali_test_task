from users.models import User
from django.db import models


class Project(models.Model):
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Заказчик'
    )
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    deadline = models.DateField(
        null=True,
        blank=True,
        verbose_name='Крайний срок'
    )
    STATUS_CHOICES = [
        ('Open', 'Открыт'),
        ('Closed', 'Закрыт'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Open',
        verbose_name='Статус'
    )


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