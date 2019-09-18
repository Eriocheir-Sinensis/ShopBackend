from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from .models import Crab
from .serializers import CrabSerializer


class CrabViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (AllowAny, )
    queryset = Crab.objects.all()
    serializer_class = CrabSerializer

