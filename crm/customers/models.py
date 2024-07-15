from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Record(models.Model):  # type: ignore
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    created_at = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.email}"
