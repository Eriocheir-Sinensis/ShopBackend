from rest_framework import serializers
from .models import Money


class MoneySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Money
        fields = (
            "description",
            "image"
        )

    def get_image(self, obj):
        return obj.pic.url
