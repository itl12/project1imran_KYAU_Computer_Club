# Generated by Django 5.0 on 2024-09-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0003_notice_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='slug',
            field=models.SlugField(blank=True, unique=True, max_length=300),
        ),
    ]
