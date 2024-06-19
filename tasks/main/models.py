from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords

# Create your models here.


class Task(models.Model):
    AVAILABLE_STATUS = [("N", "NEW"), ("IP", "IN PROGRESS"), ("R", "RESOLVED")]
    name = models.CharField(max_length=15)
    description = models.TextField(null=True)
    status = models.CharField(max_length=15, choices=AVAILABLE_STATUS, default="N")
    assigned_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.name
