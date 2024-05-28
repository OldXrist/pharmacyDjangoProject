from django.contrib.auth.models import User
from django.db import models
from shop.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total = models.PositiveIntegerField(default=0)
    address = models.TextField(max_length=100, default='')

    def __str__(self):
        return f'Order #{self.id}'


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'Order #{self.order.id}, {self.product.name} x{self.quantity}'