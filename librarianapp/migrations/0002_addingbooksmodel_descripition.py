# Generated by Django 4.0.6 on 2022-08-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarianapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='addingbooksmodel',
            name='descripition',
            field=models.CharField(help_text='descripition', max_length=300, null=True),
        ),
    ]