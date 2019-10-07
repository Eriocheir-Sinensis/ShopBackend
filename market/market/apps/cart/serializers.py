from .models import Customer
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate
from .models import Cart, CartLineItem
from ..goods.models import Crab
from ..goods.serializers import CrabSerializer


class CartLineItemSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    cart = serializers.PrimaryKeyRelatedField(queryset=Cart.objects.all(), write_only=True)
    crab = serializers.PrimaryKeyRelatedField(queryset=Crab.objects.all())
    amount = serializers.IntegerField(default=0, min_value=0)
    subtotal = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = CartLineItem
        fields = (
            "id",
            "cart",
            "crab",
            "amount",
            "subtotal",
        )

    def get_subtotal(self, obj):
        return obj.amount * obj.crab.price


class CartLineItemDetailedSerializer(CartLineItemSerializer):
    crab = CrabSerializer(read_only=True)


class CartSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='cid', read_only=True)
    customer = serializers.PrimaryKeyRelatedField(queryset=Customer.objects.all())
    items = CartLineItemSerializer(many=True, source='cart_line_items', read_only=True)
    count = serializers.SerializerMethodField(read_only=True)
    total = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Cart
        fields = (
            "id",
            "customer",
            "items",
            "count",
            "total"
        )
    
    def __init__(self, *args, **kwargs):
        super(CartSerializer, self).__init__(*args, **kwargs)
        try:
            if self.context['request'].query_params.get('detail', False):
                self.fields['items'] = CartLineItemDetailedSerializer(many=True, source='cart_line_items', read_only=True)
        except KeyError:
            pass

    def get_count(self, obj):
        return sum([i.amount for i in obj.cart_line_items.all()])

    def get_total(self, obj):
        return sum([i.amount * i.crab.price for i in obj.cart_line_items.all()])
