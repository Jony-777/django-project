import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_online.settings')
django.setup()

from products.models import Category, Product

# Crear categorías
cat_electronics = Category.objects.create(name='Electrónica')
cat_clothing = Category.objects.create(name='Ropa')
cat_books = Category.objects.create(name='Libros')

# Crear productos
Product.objects.create(
    name='Laptop HP Pavilion',
    category=cat_electronics,
    description='Laptop HP Pavilion 15.6 pulgadas, 16GB RAM, 512GB SSD',
    price=899.99,
    is_active=True
)

Product.objects.create(
    name='Smartphone Samsung Galaxy S24',
    category=cat_electronics,
    description='Samsung Galaxy S24, 128GB, pantalla AMOLED 6.2 pulgadas',
    price=749.50,
    is_active=True
)

Product.objects.create(
    name='Camiseta Nike Dri-FIT',
    category=cat_clothing,
    description='Camiseta deportiva Nike Dri-FIT, talla M, color negro',
    price=35.99,
    is_active=True
)

Product.objects.create(
    name='Python Crash Course',
    category=cat_books,
    description='Libro de programación Python para principiantes, 3ra edición',
    price=29.99,
    is_active=True
)

print("Datos de ejemplo insertados correctamente!")
print(f"Categorías: {Category.objects.count()}")
print(f"Productos: {Product.objects.count()}")
