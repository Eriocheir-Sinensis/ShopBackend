from rest_framework import serializers


class CrabSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        request = self.context.get('request')
        return {
            'id': instance.cid,
            'name': instance.name,
            'size': instance.size,
            'price': "{}{}".format(instance.price, instance.net),
            'original_price': "{}{}".format(instance.original_price, instance.net) if instance.original_price else None,
            'description': instance.description,
            'images': [request.build_absolute_uri(i.pic.url) for i in instance.images.all()]
        }
