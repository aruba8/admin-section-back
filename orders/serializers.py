from rest_framework import serializers

from orders.models import OrderType, Order
from workers.models import Worker
from workers.serializers import WorkerSerializer
from users.serializers import UserSerializer


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    assigned_to = WorkerSerializer(read_only=True)
    order_type = OrderTypeSerializer(read_only=True)
    created_by = UserSerializer(read_only=True)

    def update(self, instance, validated_data):
        assigned_to = self.initial_data['assigned_to']
        order_type = self.initial_data['order_type']
        instance.assigned_to = Worker.objects.get(pk=assigned_to)
        instance.order_description = validated_data['order_description']
        instance.order_status = validated_data['order_status']
        instance.order_type = OrderType.objects.get(pk=order_type)
        instance.save()
        return instance
        
    class Meta:
        model = Order
        fields = '__all__'
