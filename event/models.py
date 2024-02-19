from django.db import models

from event.validators import validate_future_date
from user.models import User


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=512)
    date = models.DateField(validators=[validate_future_date])
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
