# Generated by Django 5.1.7 on 2025-03-21 02:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2025, 3, 21, 2, 43, 36, 752309, tzinfo=datetime.timezone.utc)),
        ),
    ]
