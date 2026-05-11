from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "description",
            "price",
            "currency",
            "unit",
            "moq",
            "country",
            "city",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]