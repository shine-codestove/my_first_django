# Generated by Django 4.2.2 on 2023-07-04 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_person_sex'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.JSONField(default=''),
        ),
    ]
