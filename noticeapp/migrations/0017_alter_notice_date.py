# Generated by Django 5.0 on 2024-09-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0016_remove_notice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateField(verbose_name='Will be held on or from today'),
        ),
    ]
