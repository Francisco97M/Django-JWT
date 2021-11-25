from rest_framework import serializers
from .models import Status, Orders, OrderProduct
from restaurant.serializer import RestaurantSerializer
from users.serializers import UserSerializer
from product.serializer import ProductSerializer
# Create a model serializer


class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ['description']


class OrdersSerializer(serializers.ModelSerializer):
    status = StatusSerializer()
    products = StatusSerializer()
    user = UserSerializer()
    restaurant = RestaurantSerializer()

    # specify model and fields

    class Meta:
        model = Orders
        fields = ['user', 'time', 'restaurant', 'status', 'products']


class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    order = OrdersSerializer()
    product = ProductSerializer()
    # specify model and fields

    class Meta:
        model = OrderProduct
        fields = ['order', 'product', 'quantity']
