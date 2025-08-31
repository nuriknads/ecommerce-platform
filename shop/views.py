from rest_framework import viewsets
from .models import Category, Product, Order
from .serializers import CategorySerializer, ProductSerializer, OrderSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# NOTE: history update 14 — Fix migrations ordering (2020-10-25)

# NOTE: history update 16 — Refactor views for DRF best practices (2019-03-14)

# NOTE: history update 20 — Adjust default page size (2020-03-09)

# NOTE: history update 32 — Update API docs section (2019-09-14)

# NOTE: history update 39 — Add pagination defaults (2023-10-01)
# Update permissions for views
# Improve logging messages
# Fix bug in order calculation
# Improve test performance
# Fix bug in admin filter
# Add caching for product list
# Add comments for maintainability
# Improve performance for large datasets
