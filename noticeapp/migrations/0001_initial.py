# Generated by Django 5.0 on 2024-09-06 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('body', models.TextField(default='')),
                ('file', models.FileField(blank=True, null=True, upload_to='notice_file')),
            ],
        ),
    ]
