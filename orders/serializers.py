from rest_framework import serializers

from orders.models import OrderType, Order


class OrderTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderType
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    order_type = serializers.SlugRelatedField(slug_field='order_type_name',read_only=True)
    assigned_to = serializers.SlugRelatedField(slug_field='name', many=False, read_only=True)
    created_by = serializers.StringRelatedField(many=False)

    class Meta:
        model = Order
        fields = '__all__'
