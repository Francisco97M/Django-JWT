from .models import Restaurant, Direction
from rest_framework import serializers


class DirectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Direction
        fields = ['city', 'pc', 'street', 'int_number',
                  'ext_number', 'state', 'location']


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    direction = DirectionSerializer()

    class Meta:
        model = Restaurant
        fields = ['name', 'schedule_open', 'schedule_close',
                  'direction', 'phone_number', 'restaurant_type']

# , 'restaurant_type'
