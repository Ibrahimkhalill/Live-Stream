# Generated by Django 4.2.16 on 2024-11-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_device_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='LiveStream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stream_url', models.CharField(blank=True, max_length=500, null=True)),
                ('stream_name', models.CharField(blank=True, max_length=400, null=True)),
                ('create_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
