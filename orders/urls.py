from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'Status', StatusViewSet)
router.register(r'Orders', OrdersViewSet)
router.register(r'OrderProduct', OrderProductViewSet)


# specify URL Path for rest_framework
urlpatterns = [
    path('', include(router.urls)),
]
