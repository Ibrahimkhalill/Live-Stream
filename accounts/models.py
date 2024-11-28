from django.contrib.auth.models import User
from django.db import models
from django.conf import settings

class DeviceInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    deviceID = models.CharField(max_length=255, null=True, blank=True)
    device_info = models.JSONField(null=True, blank=True)
    # Define related_name to avoid clash with default auth.User model


class LiveStream(models.Model):

    stream_url = models.CharField(max_length=500, blank=True, null=True)
    stream_name = models.CharField(max_length=400, null=True, blank=True)
    create_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.stream_name

