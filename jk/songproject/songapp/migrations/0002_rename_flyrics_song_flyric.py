# Generated by Django 4.2.3 on 2023-08-01 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='flyrics',
            new_name='flyric',
        ),
    ]
