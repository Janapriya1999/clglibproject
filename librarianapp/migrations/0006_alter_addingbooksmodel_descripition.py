# Generated by Django 4.0.6 on 2022-11-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarianapp', '0005_alter_return_book_return_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addingbooksmodel',
            name='descripition',
            field=models.TextField(help_text='descripition', null=True),
        ),
    ]
