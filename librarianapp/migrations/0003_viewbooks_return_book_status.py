# Generated by Django 4.0.6 on 2022-08-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarianapp', '0002_addingbooksmodel_descripition'),
    ]

    operations = [
        migrations.AddField(
            model_name='viewbooks',
            name='return_book_status',
            field=models.CharField(default='None', max_length=50),
        ),
    ]
