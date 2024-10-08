# Generated by Django 5.0 on 2024-10-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_rename_passions_student_model_passion'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_model',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=3, null=True),
        ),
        migrations.AddField(
            model_name='student_model',
            name='phone_number',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]
