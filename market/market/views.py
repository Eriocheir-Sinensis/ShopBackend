from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import Crab, Customer
from .serializers import CrabSerializer, CustomerSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['username'] = data['phone']
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CrabViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Crab.objects.all()
        serializer = CrabSerializer(queryset, context={'request': request}, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Crab.objects.all()
        crab = get_object_or_404(queryset, pk=pk)
        serializer = CrabSerializer(crab, context={'request': request})
        return Response(serializer.data)
