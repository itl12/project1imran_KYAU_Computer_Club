# Generated by Django 5.0 on 2024-09-30 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_student_model_passion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_model',
            old_name='passion',
            new_name='passions',
        ),
    ]
