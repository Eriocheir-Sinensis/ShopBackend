from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Crab
from .serializers import CrabSerializer


class CrabViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Crab.objects.all()
        serializer = CrabSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Crab.objects.all()
        crab = get_object_or_404(queryset, pk=pk)
        serializer = CrabSerializer(crab)
        return Response(serializer.data)
