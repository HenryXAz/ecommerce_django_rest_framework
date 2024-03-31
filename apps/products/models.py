from django.db import models

# base model
from apps.base.models import BaseModel


# Create your models here.
class MeasureUnit(BaseModel):
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Measure Unit'
        verbose_name_plural = 'Measure Units'

    def __str__(self):
        return self.description


class Category(BaseModel):
    description = models.CharField('Descripción', max_length=50, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.description


class Indicator(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Indicator discount'
        verbose_name_plural = 'Indicators discount'

    def __str__(self):
        return f'Discount of category {self.category_product} : {self.discount_value}'


class Product(BaseModel):
    name = models.CharField(max_length=150, unique=True, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, null=True)
    category_product = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


def __str__(self):
    return self.name
