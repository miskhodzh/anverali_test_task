# Generated by Django 4.2 on 2024-05-05 05:52

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_rating_user_successful_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='successful_projects',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]
