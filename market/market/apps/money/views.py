from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from .models import Money
from .serializers import MoneySerializer


class MoneyViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    queryset = Money.objects.filter(enabled=True)
    serializer_class = MoneySerializer
