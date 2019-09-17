from .models import Customer
from rest_framework import serializers
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, password_validation
from rest_framework.validators import UniqueValidator


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = (
            "cid",
            "name",
            "phone",
            "address"
        )


class AuthTokenSerializer(serializers.Serializer):
    phone = serializers.CharField(label="phone")
    password = serializers.CharField(label="password")

    def validate(self, attrs):
        phone = attrs.get('phone')
        password = attrs.get('password')

        if phone and password:
            user = authenticate(username=phone, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError(_("User account is disabled."))
            else:
                raise serializers.ValidationError(_("User not found."))
        else:
            raise serializers.ValidationError(_('Must include "phone" and "password".'))
        attrs['user'] = user
        return attrs


class CreateCustomerSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=15, required=True, validators=[UniqueValidator(queryset=Customer.objects.all())])
    name = serializers.CharField(max_length=64, required=True)
    address = serializers.CharField(max_length=200, required=False, allow_blank=True)

    class Meta:
        model = Customer
        fields = ('phone', 'name', 'address', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value

    def validate_name(self, value):
        return value

    def validate_address(self, value):
        # TODO: validate address
        return value

    def create(self, validated_data):
        user = Customer(
            username=validated_data['phone'],
            phone=validated_data['phone'],
            name=validated_data['name'],
            address=validated_data.get('address', None))
        user.set_password(validated_data['password'])
        user.save()
        return user
