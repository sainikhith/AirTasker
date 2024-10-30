from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def latest_by_user(self, user):
        return Task.user.filter(user=user).order_by('-created_at').first()

    def is_completed(self):
        return self.completed

    def __str__(self):
        return self.title