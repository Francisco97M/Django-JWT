from rest_framework import viewsets
from .serializer import StatusSerializer, OrdersSerializer, OrderProductSerializer
from .models import Status, Orders, OrderProduct
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from users.views import verify_token


class StatusViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class OrderProductViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer


class StoreView(APIView):
    def get(self, request):
        payload = verify_token(request)
        store = Orders.objects.all()
        serializer = OrdersSerializer(store, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass

    def delete(self, request):
        pass

    def put(self, request):
        pass

    def patch(self, request):
        pass
