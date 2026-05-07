from django.shortcuts import render
from .permissions import IsSupplier
from rest_framework.permissions import BasePermission
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny 
from drf_spectacular.utils import extend_schema, OpenApiResponse

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserRegisterSerializer, CustomTokenSerializer


@extend_schema(
    request=UserRegisterSerializer,
    responses={201: UserRegisterSerializer},
    description="Supplier registration endpoint (no auth required)"
)

class UserRegisterView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(request=UserRegisterSerializer)
    def post(self, request):
        
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()

            return Response(
                {
                    "message": "User registered successfully",
                    "user": {
                        "email": user.email,
                        "business_name": user.business_name
                    }
                },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LoginView(TokenObtainPairView): 
    serializer_class = CustomTokenSerializer

    @extend_schema(
        request=CustomTokenSerializer,
        responses={200: OpenApiResponse(description="JWT tokens returned")},
        description="Login supplier and return JWT tokens"
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
    
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token required"},
                status=400
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"detail": "Logout successful"}, status=200)
        except Exception:
            return Response({"detail": "Invalid token"}, status=400)
            
            
class SupplierDashboardView(APIView):
    permission_classes = [IsAuthenticated, IsSupplier]
    def get(self, request):
        return Response({
            "message": "Welcome Supplier"
        })            
        
        



class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role == "admin"
        )