from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # still required by Django
    def __str__(self):
        return self.email

class GlassesLocation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="locations")
    glasses_id = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)   # e.g. 24.8607
    longitude = models.DecimalField(max_digits=9, decimal_places=6)  # e.g. 67.0011
    timestamp = models.DateTimeField(auto_now=True)  # auto-updates each time location is updated

    def __str__(self):
        return f"{self.glasses_id} - {self.latitude}, {self.longitude}"

