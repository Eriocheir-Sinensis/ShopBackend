from rest_framework import status, viewsets, mixins
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.authtoken import views
from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in
from .models import Customer
from .serializers import CustomerSerializer, AuthTokenSerializer, CreateCustomerSerializer


class CustomerViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )


class CustomerSelfViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, *args, **kwargs):
        instance = self.request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.ObtainAuthToken, viewsets.ViewSet):
    serializer_class = AuthTokenSerializer
    permission_classes = (AllowAny, )

    def log(self, request, *args, **kwargs):
        status_code = status.HTTP_200_OK
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        serialized = CustomerSerializer(user, context={'request': request}).data
        token, created = Token.objects.get_or_create(user=user)
        serialized['token'] = token.key
        user_logged_in.send(sender=user.__class__, request=request, user=user)
        return Response(serialized, status=status_code)


class CustomerCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Customer.objects.all()
    permission_classes = (AllowAny, )
    serializer_class = CreateCustomerSerializer

    def perform_create(self, serializer):
        instance = serializer.save()
        self.user = instance

    def create(self, request, *args, **kwargs):
        try:
            serializer = AuthTokenSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.user = serializer.validated_data['user']
            serialized = CustomerSerializer(self.user, context={'request': request}).data
            status_code = status.HTTP_200_OK
        except Exception:
            try:
                super(CustomerCreateViewSet, self).create(request, args, kwargs)
                serialized = CustomerSerializer(self.user, context={'request': request}).data
                status_code = status.HTTP_201_CREATED
            except ValidationError as e:
                if 'phone' in e.detail and 'unique' in e.detail['phone'][0]:
                    return Response({'msg': "帐号已经存在"}, status.HTTP_400_BAD_REQUEST)
                else:
                    raise e
        # TODO: verify phone
        # phone = request.data.get('phone', None)
        token, created = Token.objects.get_or_create(user=self.user)
        serialized['token'] = token.key
        return Response(serialized, status=status_code)
