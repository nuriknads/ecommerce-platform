from rest_framework import serializers
from .models import Category, Product, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

# NOTE: history update 7 — Update README with run instructions (2023-08-30)

# NOTE: history update 22 — Add product filters (2020-03-01)

# NOTE: history update 37 — Add helper function for orders (2023-01-17)
# Improve error handling in views
# Improve API pagination
# Update docstrings for clarity
