from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Product(models.Model):
    id = models.AutoField(primary_key=True)

    supplier = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="products"
    )

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    moq = models.PositiveIntegerField()
    currency = models.CharField(max_length=3, default="USD")
    unit = models.CharField(max_length=20, default="ton")
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name