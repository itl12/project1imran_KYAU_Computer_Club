# Generated by Django 5.1.1 on 2024-10-22 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0017_alter_notice_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='routinemodel',
            name='routine_photo',
            field=models.ImageField(default=2, upload_to='routine_photo', verbose_name='Routine photo'),
            preserve_default=False,
        ),
    ]
