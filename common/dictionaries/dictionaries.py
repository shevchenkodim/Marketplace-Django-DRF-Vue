from common.dictionaries.base import Dictionaries
from common.products.categories.categories import CategoryModel
from django.db import models


class UnitDict(Dictionaries):

    def __str__(self):
        return f'{self.value} [{self.code}]'


class CharacteristicHandbook(Dictionaries):
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value} [{self.code}]'
