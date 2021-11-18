from rest_framework import serializers
from .models import Category, Product, CartProduct, Cart, Customer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CartProductSerializer(serializers.ModelSerializer):

    product = ProductsViewSerializer()

    class Meta:
        model = CartProduct
        fields = ['id', 'product', 'qty', 'final_price']



class CustumersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'