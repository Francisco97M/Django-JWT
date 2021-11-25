from .models import Direction, Restaurant
from rest_framework import viewsets
from .serializer import DirectionSerializer, RestaurantSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.views import verify_token


class DirectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Direction.objects.all()
    serializer_class = DirectionSerializer


class RestaurantViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
