from rest_framework import serializers
from .models import Crab, LineItem


class CrabSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='cid')
    images = serializers.SerializerMethodField()

    class Meta:
        model = Crab
        fields = (
            "id",
            "name",
            "size",
            "price",
            "original_price",
            "net",
            "description",
            "images"
        )

    def get_images(self, obj):
        request = self.context.get('request')
        return [request.build_absolute_uri(i.pic.url) for i in obj.images.all()]
