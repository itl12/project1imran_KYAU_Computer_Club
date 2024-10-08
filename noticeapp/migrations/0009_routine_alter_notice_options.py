# Generated by Django 5.0 on 2024-09-11 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticeapp', '0008_alter_notice_body'),
    ]

    operations = [
        migrations.CreateModel(
            name='Routine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to='notice_file')),
                ('date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
            options={
                'ordering': ['update_date'],
            },
        ),
        migrations.AlterModelOptions(
            name='notice',
            options={'ordering': ['-id']},
        ),
    ]
