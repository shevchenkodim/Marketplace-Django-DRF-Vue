from common.dictionaries.base import Dictionaries
from common.products.categories.categories import CategoryModel
from django.db import models


class CurrencyDict(Dictionaries):
    """ Currency dict model """

    def __str__(self):
        return f'{self.value} [{self.code}]'

    class Meta:
        db_table = 'dict_currency'


class UnitDict(Dictionaries):
    """ Units dict model """

    def __str__(self):
        return f'{self.value} [{self.code}]'

    class Meta:
        db_table = 'dict_unit'


class CharacteristicHandbookDict(Dictionaries):
    """ Characteristic handbook dict model """
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} [{self.code}]'

    class Meta:
        db_table = 'dict_characteristic_handbook'


class BrandDict(Dictionaries):
    """ Product brand dict model """
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.value} [{self.code}]'

    class Meta:
        db_table = 'dict_brand'
        ordering = ['value']
