from rest_framework import serializers

from orders.models import OrderType, Order
from workers.serializers import WorkerSerializer
from users.serializers import UserSerializer


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    assigned_to = WorkerSerializer(read_only=False)
    order_type = OrderTypeSerializer(read_only=False)
    created_by = UserSerializer(read_only=False)

    class Meta:
        model = Order
        fields = '__all__'
