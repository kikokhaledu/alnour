from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'date_time', 'user')
    search_fields = ('title', 'user__email')
    list_filter = ('date_time',)
