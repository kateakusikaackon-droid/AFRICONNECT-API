from rest_framework import serializers
from .models import SupplierProfile


class SupplierProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = SupplierProfile
        fields = [
            "id",
            "user",
            "phone_number",
            "country_region",
            "gender",
            "image",
            "created_at",
        ]
        read_only_fields = ["id", "user", "created_at"]