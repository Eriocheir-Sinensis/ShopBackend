from .models import Customer
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from .models import Order, OrderLineItem
from ..goods.models import Crab
from ..goods.serializers import CrabSerializer


class OrderLineItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    crab = serializers.PrimaryKeyRelatedField(queryset=Crab.objects.all())
    amount = serializers.IntegerField(default=0, min_value=0)
    subtotal = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = OrderLineItem
        fields = (
            "id",
            "crab",
            "amount",
            "subtotal",
        )

    def get_subtotal(self, obj):
        return obj.amount * obj.crab.price


class OrderLineItemDetailedSerializer(OrderLineItemSerializer):
    crab = CrabSerializer(read_only=True)


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='oid', read_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all(), required=False)
    status = serializers.CharField(read_only=True)
    receiver_name = serializers.CharField(required=True)
    receiver_phone = serializers.CharField(required=True)
    receiver_address = serializers.CharField(required=True)
    items = OrderLineItemSerializer(many=True, source='order_line_items')
    count = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "customer",
            "status",
            "receiver_name",
            "receiver_phone",
            "receiver_address",
            "items",
            "count",
            "total"
        )

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].query_params.get('detail', False):
                self.fields['items'] = OrderLineItemDetailedSerializer(many=True, source='order_line_items',
                                                                      read_only=True)
        except KeyError:
            pass

    def get_count(self, obj):
        return sum([i.amount for i in obj.order_line_items.all()])

    def get_total(self, obj):
        return sum([i.amount * i.crab.price for i in obj.order_line_items.all()])

    def validate(self, attrs):
        if len(attrs.get('order_line_items', [])) <= 0:
            raise serializers.ValidationError("订单中没有商品")
        return super().validate(attrs)

    def create(self, validated_data):
        items = validated_data.pop('order_line_items')
        validated_data['customer'] = self.context.get('request').user
        order = Order.objects.create(**validated_data)
        OrderLineItem.objects.bulk_create([
            OrderLineItem(order=order, **item)
            for item in items
        ])
        return order
