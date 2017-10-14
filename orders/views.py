# Create your views here.
from rest_framework import viewsets

from orders.models import Order, OrderType
from orders.serializers import OrderSerializer, OrderTypeSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows orders to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderTypesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows order types to be viewed or edited.
    """
    queryset = OrderType.objects.all()
    serializer_class = OrderTypeSerializer
