# Generated by Django 5.0 on 2024-09-07 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleryapp', '0005_alter_activity_gallery_options_activity_gallery_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity_gallery',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
