# Generated by Django 4.2.16 on 2024-11-28 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_deviceinfo_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livestream',
            name='user',
        ),
    ]