# Generated by Django 4.0.6 on 2022-08-13 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='studentRegisterModel',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('student_fullname', models.CharField(default=True, help_text='student_fullname', max_length=100)),
                ('student_branch', models.CharField(default=True, help_text='student_branch', max_length=100)),
                ('student_year', models.CharField(default=True, help_text='student_year', max_length=100)),
                ('student_email', models.EmailField(default=True, help_text='student_email', max_length=100)),
                ('student_password', models.CharField(help_text='student_password', max_length=100, null=True)),
                ('student_id', models.CharField(help_text='student_id', max_length=100, null=True)),
                ('student_photo', models.ImageField(null=True, upload_to='images/')),
                ('student_status', models.CharField(default='pending', max_length=50)),
            ],
        ),
    ]
