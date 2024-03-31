# serializers
from apps.products.api.serializers.general_serializers import (MeasureUnitSerializer, IndicatorSerializer,
                                                               CategoryProductSerializer)

# general list view
from apps.base.api import GeneralListApiView


class MeasureUnitListView(GeneralListApiView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListView(GeneralListApiView):
    serializer_class = CategoryProductSerializer


class IndicatorListView(GeneralListApiView):
    serializer_class = IndicatorSerializer
