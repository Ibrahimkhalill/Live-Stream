# Generated by Django 4.2.16 on 2024-11-28 07:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_livestream'),
    ]

    operations = [
        migrations.AddField(
            model_name='livestream',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='livestreams', to=settings.AUTH_USER_MODEL),
        ),
    ]
