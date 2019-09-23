from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Cart, CartLineItem
from .serializers import CartSerializer, CartLineItemSerializer


class CartViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartSerializer

    def get_queryset(self):
        user = self.request.user
        return Cart.objects.filter(customer=user)

    def create(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.filter(customer=user)
        if cart.exists():
            return Response(self.get_serializer(cart.first()).data, status=status.HTTP_200_OK)

        serializer = self.get_serializer(data={'customer': user.cid})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def list(self, request, *args, **kwargs):
        user = self.request.user
        cart = Cart.objects.get(customer=user)
        serializer = self.get_serializer(cart)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_200_OK, headers=headers)


class CartLineItemViewSet(mixins.DestroyModelMixin, mixins.UpdateModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = CartLineItemSerializer

    def get_queryset(self):
        return CartLineItem.objects.filter(customer=self.request.user)

    def create(self, request, *args, **kwargs):
        cart = get_object_or_404(Cart, cid=kwargs.get('cart_id', None), customer=request.user)
        crab_id = request.data.get('crab', None)
        if cart.cart_line_items.filter(crab__cid=crab_id).exists():
            # If crab already in cart.
            line_item = cart.cart_line_items.get(crab__cid=crab_id)
            line_item.amount += int(request.data.get('amount', 0))
            line_item.save()
            return Response(self.get_serializer(line_item.cart).data, status=status.HTTP_200_OK)

        data = {
            'cart': cart.cid,
            'crab': crab_id,
            'amount': request.data.get('amount', None)
        }
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        return super().update(request, args, kwargs, partial=True)
