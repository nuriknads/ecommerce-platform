from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order #{self.id}"

# NOTE: history update 1 — Improve model __str__ (2020-08-01)

# NOTE: history update 8 — Fix bug in Product serializer (2019-07-29)

# NOTE: history update 15 — Minor improvements to settings (2023-08-09)

# NOTE: history update 24 — Add helper function for orders (2023-12-30)

# NOTE: history update 26 — Minor improvements to settings (2020-12-03)

# NOTE: history update 38 — Improve model __str__ (2021-09-04)
# Fix typo in README
# Improve test performance
# Fix typo in README
# Update requirements.txt
# Fix missing import in views
# Refactor serializers for DRY principle
# Add caching for product list
# Refactor serializers for DRY principle
# Improve test performance
# Improve logging messages
# Fix serializer validation
# Add search index for products
# Improve performance for large datasets
# Add caching for product list
