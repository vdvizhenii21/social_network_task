from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserActivity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="useractivity")
    last_request = models.DateTimeField(null=True)
