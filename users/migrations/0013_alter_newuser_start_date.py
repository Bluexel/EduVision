# Generated by Django 5.0.2 on 2024-02-27 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_newuser_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 27, 10, 45, 34, 457132, tzinfo=datetime.timezone.utc)),
        ),
    ]
