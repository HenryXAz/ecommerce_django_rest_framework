# django
from django.urls import path

# views
from apps.products.api.views.general_views import MeasureUnitListView, CategoryProductListView, IndicatorListView

urlpatterns = [
  path('measure-units/', MeasureUnitListView.as_view(), name='measure-units'),
  path('categories/', CategoryProductListView.as_view(), name='product-categories'),
  path('indicators/', IndicatorListView.as_view(), name='indicators'),
]
