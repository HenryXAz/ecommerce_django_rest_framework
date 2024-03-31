# django
from django.urls import path

# views
from apps.products.api.views.general_views import MeasureUnitListView, CategoryProductListView, IndicatorListView
from apps.products.api.views.product_views import (ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView)

urlpatterns = [
  path('measure-units/', MeasureUnitListView.as_view(), name='measure-units'),
  path('categories/', CategoryProductListView.as_view(), name='product-categories'),
  path('indicators/', IndicatorListView.as_view(), name='indicators'),
  path('', ProductListCreateAPIView.as_view(), name='products_list_create'),
  path('<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product_detail'),
  # path('retrieve/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
  # path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_udpate'),
  # path('destroy/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_destroy'),
]
