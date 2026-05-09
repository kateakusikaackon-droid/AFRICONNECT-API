from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer


class ProductListCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @extend_schema(responses=ProductSerializer(many=True))
    def get(self, request):
        products = Product.objects.filter(supplier=request.user)
        
        serializer = self.serializer_class(products, many=True) 
              
        return Response({
            "message": "Products retrieved successfully",
            "products": serializer.data
        })
        
    @extend_schema(request=ProductSerializer)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(supplier=request.user)
            return Response({
                "message": "Product created successfully",
                "product": serializer.data
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    def get_object(self, user, pk):
        try:
            return Product.objects.get(id=pk, supplier=user)
        except Product.DoesNotExist:
            return None

    @extend_schema(responses=ProductSerializer)
    def get(self, request, pk):
        product = self.get_object(request.user, pk)

        if not product:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product)

        return Response({
            "message": "Product retrieved successfully",
            "product": serializer.data
        })

    @extend_schema(request=ProductSerializer)
    def put(self, request, pk):
        product = self.get_object(request.user, pk)

        if not product:
            return Response({"detail": "Not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product,data=request.data,partial=True)

        if serializer.is_valid():
            serializer.save()
            
            return Response({
            "message": "Product updated successfully",
            "product": serializer.data
            })
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(request.user, pk)

        if not product:
            return Response({"detail": "Not found"},  status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response({"message": "Deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
