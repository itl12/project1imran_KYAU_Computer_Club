# Generated by Django 5.0 on 2024-10-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('publications', models.JSONField(default=list)),
                ('academic_info', models.JSONField(default=dict)),
                ('experience', models.JSONField(default=list)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('whatsapp', models.CharField(blank=True, max_length=15, null=True)),
                ('room_number', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
