from django.test import TestCase
from .models import Product


class ProductModelTest(TestCase):

    def test_product_creation(self):
        product = Product.objects.create(
            name="Laptop",
            category="Electronics",
            price=55000,
            quantity=5
        )

        self.assertEqual(product.name, "Laptop")
        self.assertEqual(product.category, "Electronics")
        self.assertEqual(product.price, 55000)
        self.assertEqual(product.quantity, 5)

    def test_product_string(self):
        product = Product.objects.create(
            name="Mobile",
            category="Electronics",
            price=25000,
            quantity=10
        )

        self.assertEqual(str(product), "Mobile")