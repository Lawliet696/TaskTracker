# Generated by Django 5.1.5 on 2025-02-03 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task_date_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-priority'], 'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
    ]
