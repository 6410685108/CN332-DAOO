# Generated by Django 5.0.3 on 2024-03-24 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='onwer',
            new_name='owner',
        ),
    ]