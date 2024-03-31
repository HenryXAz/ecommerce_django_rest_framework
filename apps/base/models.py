from django.db import models

# Create your models here.
class BaseModel(models.Model):
  id = models.AutoField(primary_key=True)
  state = models.BooleanField('Estado', default=True)
  created_date = models.DateField('Fecha de creación', auto_now_add=True)
  modified_date = models.DateField('Fecha de modificación', auto_now=True)
  deleted_date = models.DateField('Fecha de elimianción', auto_now=True)

  class Meta:
    abstract = True
    verbose_name = 'Base Model'
    verbose_name_plural = 'Base Models'

