from .models import Category, Product, Customer, CartProduct
from .serializers import CategorySerializer, ProductsViewSerializer, ProductDetailSerializer, CustumersSerializer, \
    CartProductSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]


class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsViewSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [IsAuthenticated, ]


class CartProduct(ListAPIView):
    queryset = CartProduct
    serializer_class = CartProductSerializer


class CustomersView(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustumersSerializer
