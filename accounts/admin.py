from django.contrib import admin

from .models import LiveStream,DeviceInfo

# Register your models here.


admin.site.register(LiveStream)
admin.site.register(DeviceInfo)