from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ..cart.models import Cart
from .models import Order
from .serializers import OrderSerializer, OrderLineItemSerializer


class OrderViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = OrderSerializer

    def get_serializer_context(self):
        return {'request': self.request}

    def get_queryset(self):
        user = self.request.user
        return Order.objects.filter(customer=user)

    def create(self, request, *args, **kwargs):
        response = super().create(request, args, kwargs)
        if response.status_code == 201:
            # Clean cart after order created
            Cart.objects.get(customer=request.user).cart_line_items.all().delete()
        return response

