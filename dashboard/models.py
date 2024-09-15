from django.db import models
from django.contrib.auth.models import User

# Create your models here.
CATEGORY = (
    ('Mountain Dew', 'Mountain Dew'),
    ('Pepsi', 'Pepsi'), ('Sprite', 'Sprite'),
    ('Coca Cola', 'Coca Cola'), ('RC', 'RC'),
)


class Product(models.Model):
    name = models.CharField(max_length=100, null=True)
    quantity = models.PositiveIntegerField(null=True)
    company = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    name = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    order_quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return f'{self.customer}-{self.name}'
