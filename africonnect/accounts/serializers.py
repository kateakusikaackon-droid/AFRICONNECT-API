from rest_framework import serializers
from .models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [
            'id',
            'name',
            'business_name',
            'email',
            'password'            
        ]
        read_only_fields = ['id']

    def validate_email(self, value):
        value = value.lower()

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")

        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters")

        return value

    def create(self, validated_data):
        validated_data['email'] = validated_data['email'].lower()
        validated_data['role'] = 'supplier'
        user = User.objects.create_user(**validated_data)
        return user


class CustomTokenSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)
        
        data['name'] = self.user.name
        data['business_name'] = self.user.business_name
        data['email'] = self.user.email
        return data
    
    
    
class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(
        required=True,
        help_text="Refresh token to blacklist"
    )   
    





class DashboardSerializer(serializers.Serializer):
    message = serializers.CharField()

    profile = serializers.DictField()

    products = serializers.DictField()

    