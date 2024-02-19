from django.utils import timezone
from rest_framework.exceptions import ValidationError


def validate_future_date(value):
    if value <= timezone.now().date():
        raise ValidationError("Date cannot be in the past")
