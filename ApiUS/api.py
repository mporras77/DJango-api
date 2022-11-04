from .models import Producto

from rest_framework import viewsets, permissions
 
from .serializers import ProductoSerializer

class ProductoviewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    pagination_classes = [permissions.AllowAny]
    serializer_class = ProductoSerializer