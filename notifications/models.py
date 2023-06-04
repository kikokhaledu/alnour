from django.db import models
from users.models import User

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
