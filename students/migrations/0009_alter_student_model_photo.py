# Generated by Django 5.0 on 2024-09-19 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_alter_student_model_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_model',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='students_profile_pic'),
        ),
    ]
