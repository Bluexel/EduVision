# Generated by Django 5.0.2 on 2024-02-24 16:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 24, 16, 40, 47, 375480, tzinfo=datetime.timezone.utc)),
        ),
    ]
