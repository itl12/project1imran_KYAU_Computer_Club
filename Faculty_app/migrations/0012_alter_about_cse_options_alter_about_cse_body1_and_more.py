# Generated by Django 5.1.1 on 2024-10-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Faculty_app', '0011_about_cse'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about_cse',
            options={'verbose_name_plural': 'About CSE Dept. Head Message'},
        ),
        migrations.AlterField(
            model_name='about_cse',
            name='body1',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='about_cse',
            name='body2',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
