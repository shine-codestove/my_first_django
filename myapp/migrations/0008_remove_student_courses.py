# Generated by Django 4.2.2 on 2023-07-06 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_studentcourse'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
    ]
