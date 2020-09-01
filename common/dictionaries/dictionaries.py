from common.dictionaries.base import Dictionaries
from common.products.categories.categories import CategoryModel
from django.db import models


class CharacteristicDict(Dictionaries):
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
