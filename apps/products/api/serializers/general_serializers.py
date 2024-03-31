# rest framework
from rest_framework import serializers

# models
from apps.products.models import MeasureUnit, Category, Indicator


class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)


class CategoryProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)

class IndicatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Indicator
        exclude = ('state','created_date', 'modified_date', 'deleted_date',)
