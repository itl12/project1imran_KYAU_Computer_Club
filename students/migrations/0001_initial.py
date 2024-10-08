# Generated by Django 5.0 on 2024-09-12 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='students_photo/')),
                ('name', models.CharField(max_length=40)),
                ('batch', models.IntegerField()),
                ('std_id', models.CharField(max_length=16)),
                ('description', models.TextField(blank=True, null=True)),
                ('cv', models.FileField(blank=True, null=True, upload_to='students_cv/')),
                ('skills', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'ordering': ['-batch', 'std_id'],
            },
        ),
    ]
