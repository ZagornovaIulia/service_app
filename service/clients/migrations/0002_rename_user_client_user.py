# Generated by Django 4.2.6 on 2023-10-18 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='User',
            new_name='user',
        ),
    ]
