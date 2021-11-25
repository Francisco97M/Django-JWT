from django.db import models
from restaurant.models import Restaurant
from product.models import Product
from django.conf import settings
from users.models import User


class Status(models.Model):
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.description


class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    products = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.id)


class OrderProduct(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product

# Create your models here.
