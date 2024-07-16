from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Record(models.Model):
    first_name = models.CharField(max_length=100)  # type: ignore
    last_name = models.CharField(max_length=100)  # type: ignore
    email = models.EmailField(unique=True)  # type: ignore
    phone = models.CharField(max_length=20)  # type: ignore
    address = models.CharField(max_length=100)  # type: ignore
    city = models.CharField(max_length=50)  # type: ignore
    region = models.CharField(max_length=50)  # type: ignore
    zipcode = models.CharField(max_length=10)  # type: ignore
    created_at = models.DateTimeField(default=timezone.now)  # type: ignore
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # type: ignore

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} - {self.email}"
