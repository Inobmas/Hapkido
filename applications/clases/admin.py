from django.contrib import admin
from .models import Group, TimeZone, TimeZoneGroup, Training, Campus

admin.site.register(Group)
admin.site.register(TimeZone)
admin.site.register(TimeZoneGroup)
admin.site.register(Training)
admin.site.register(Campus)

