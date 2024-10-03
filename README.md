# 🛒 Django E-commerce API

**Описание:**  
REST API для интернет-магазина, реализованный на Django + Django REST Framework.  
Функционал:
- Управление категориями товаров
- Управление товарами
- Создание заказов
- API с сериализацией данных (DRF)

---

## 🚀 Стек технологий:
- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (по умолчанию)
- Git / GitHub

---

## 🔗 API эндпоинты:
- `GET /api/categories/` — список категорий
- `GET /api/products/` — список товаров
- `GET /api/orders/` — список заказов

---

## ▶ Запуск проекта:
```bash
git clone https://github.com/nuriknads/ecommerce-platform.git
cd ecommerce-platform
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Update 12: Improve model __str__ — 2023-05-23

Update 27: Refactor views for DRF best practices — 2023-03-05

Update 34: Update docstrings — 2022-12-22

Update 35: Improve API response for products — 2019-09-30
# Add product search feature
# Add filtering for products
# Add constants for repeated values
# Refactor model relationships
# Improve model __str__ representation
# Refactor views for clarity
# Fix serializer validation
# Add caching for product list
# Refactor serializers for DRY principle
