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
        ('Progress', 'В процессе'),
        ('Closed', 'Закрыт'),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='Open',
        verbose_name='Статус'
    )

    def get_fields(self):
        return [
            self.id,
            self.customer,
            self.title,
            self.price,
            self.description,
            self.pub_date,
            self.deadline,
            self.status,
        ]
    @classmethod
    def get_verbose_names(cls):
        return [field.verbose_name for field in cls._meta.fields]
