from rest_framework import serializers
from .models import SupplierProfile


class SupplierProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierProfile
        fields = [
            "id",
            "user",
            "contact",
            "country",
            "city",
            "image",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]