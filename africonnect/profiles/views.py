from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

from .models import SupplierProfile
from .serializers import SupplierProfileSerializer


class SupplierProfileView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SupplierProfileSerializer

    @extend_schema(responses=SupplierProfileSerializer)
    def get(self, request):
        try:
            profile = SupplierProfile.objects.get(user=request.user)
            
        except SupplierProfile.DoesNotExist:
            return Response(
                {"detail": "Profile not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer =  self.serializer_class(profile)
        
        return Response({
            "message": "Profile retrieved successfully",
            "profile": serializer.data
        }, status=status.HTTP_200_OK)
        
    @extend_schema(request=SupplierProfileSerializer, responses=SupplierProfileSerializer)
    def put(self, request):
        profile, created = SupplierProfile.objects.get_or_create(user=request.user)

        serializer =self.serializer_class(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({
                "message": "Profile updated successfully",
                "profile": serializer.data
            }, status=status.HTTP_200_OK)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)