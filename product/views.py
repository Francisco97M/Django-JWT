from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductSerializer
from .models import Product
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.views import verify_token


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class StoreView(APIView):
    def get(self, request):
        payload = verify_token(request)
        store = Product.objects.all()
        serializer = ProductSerializer(store, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass
