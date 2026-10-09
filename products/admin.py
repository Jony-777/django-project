from django.contrib import admin
from .models import Category, Product


# Registrar modelos en el administrador
admin.site.register(Category)
admin.site.register(Product)
