from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter
from .views import CartViewSet, CartLineItemViewSet

cart_router = DefaultRouter()
cart_router.register(r'', CartViewSet, basename='cart')

line_item_router = DefaultRouter()
line_item_router.register(r'', CartLineItemViewSet, basename='cart_line_item')

urlpatterns = [
    re_path(r'^(?P<cart_id>[\w]+)/', include(line_item_router.urls)),
    re_path(r'^$', include(cart_router.urls)),
]
