from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class SupplierProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    phone_number = models.CharField(max_length=20)
    country_region = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    image = models.ImageField(upload_to="profiles/", null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} Profile"