# Generated by Django 5.1 on 2024-08-19 20:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='ingreso',
            field=models.DateField(default=datetime.date.today),
        ),
    ]