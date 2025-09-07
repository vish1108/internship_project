from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.utils.timezone import now


# class TaskQuerySet(models.QuerySet):
#     def completed_last_week(self, user):
#         last_week = timezone.now() - timedelta(days=7)
#         return self.filter(user = user, status ="completed", updated_at__gte=last_week)

class TaskQuerySet(models.QuerySet):
    def completed_last_week(self, user):
        # today = now().date()
        one_week_ago = timezone.now() - timedelta(days=7)
        return self.filter(
            user=user,
            status="completed",
            updated_at__gte=one_week_ago
        )
    
    def pending_task(self, user):
        return self.filter(user=user, status = "pending")


# class TaskQuerySet(models.QuerySet):
#     def completed_last_week(self, user):
#         last_week = timezone.now() - timedelta(days=7)

class Task(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("in_progress", "In Progress"),
        ("completed", "Completed"),
    ]


    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="task")
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default="pending")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = TaskQuerySet.as_manager()


    def __str__(self):
        return self.title
