from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreateAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDestroyAPIView(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer




