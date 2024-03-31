# rest framework
from rest_framework import serializers

# models
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state',)
