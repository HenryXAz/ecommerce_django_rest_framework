from django.contrib import admin
from apps.products.models import *


class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'state',)


class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'state',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'state',)

    
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'state',)


# Register your models here.
admin.site.register(MeasureUnit, MeasureUnitAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Indicator)
admin.site.register(Product, ProductAdmin)
