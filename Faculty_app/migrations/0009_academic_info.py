# Generated by Django 5.0 on 2024-10-02 14:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty_app', '0008_rename_data_research_and_publication_research_and_publication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Academic_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=60)),
                ('institution', models.CharField(max_length=60)),
                ('period', models.CharField(max_length=60)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_info', to='Faculty_app.faculty_profile')),
            ],
        ),
    ]
