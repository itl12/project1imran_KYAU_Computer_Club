# Generated by Django 5.0 on 2024-09-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_student_model_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
