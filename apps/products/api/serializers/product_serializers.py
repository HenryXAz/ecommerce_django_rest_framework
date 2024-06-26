# rest framework
from rest_framework import serializers

# models
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image if instance.image != '' else '',
            'measure_unit': {
                'description': instance.measure_unit.description,
                'id': instance.measure_unit.id,
            } if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else '',
        }
    
    def validate_image(self, value):
        if value == None:
            return ''
        return value
