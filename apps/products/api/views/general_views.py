# rest framework
from rest_framework import generics

# serializers
from apps.products.api.serializers.general_serializers import (MeasureUnitSerializer, IndicatorSerializer,
                                                               CategoryProductSerializer)

# models
from apps.products.models import MeasureUnit, Category, Indicator


class MeasureUnitListView(generics.ListAPIView):
    serializer_class = MeasureUnitSerializer

    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)


class CategoryProductListView(generics.ListAPIView):
    serializer_class = CategoryProductSerializer

    def get_queryset(self):
        return Category.objects.filter(state=True)


class IndicatorListView(generics.ListAPIView):
    serializer_class = IndicatorSerializer

    def get_queryset(self):
        return Indicator.objects.filter(state=True)
