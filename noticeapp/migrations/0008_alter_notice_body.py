# Generated by Django 5.0 on 2024-09-07 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0006_rename_file_notice_pdf_notice_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
