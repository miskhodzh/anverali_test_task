# Generated by Django 4.2 on 2024-05-05 06:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_successful_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='successful_projects',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, validators=[django.core.validators.MaxValueValidator(1000000)]),
        ),
    ]