# Generated by Django 4.2.9 on 2024-05-11 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_newuser_start_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=200)),
                ('user_id', models.IntegerField()),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
            ],
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
