# Generated by Django 5.0 on 2024-09-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0009_routine_alter_notice_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='routine',
            name='pdf',
        ),
        migrations.AddField(
            model_name='routine',
            name='routine_pdf',
            field=models.FileField(default='none', upload_to='notice_file', verbose_name='Routine pdf'),
            preserve_default=False,
        ),
    ]
