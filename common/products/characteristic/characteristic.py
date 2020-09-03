from django.db import models

from common.dictionaries.dictionaries import CharacteristicHandbookDict, UnitDict
from common.products.categories.categories import CategoryModel
from common.products.product.product import Product

CHOICE_FIELDS_TYPE = [
    ('Text', 'Text'),
    ('Integer', 'Integer'),
    ('Float', 'Float'),
    ('Boolean', 'Boolean'),
]


class CharacteristicAttributes(models.Model):
    """ Characteristic attributes models """
    FIELDS_TEXT = 'Text'
    attribute_id = models.ForeignKey(CharacteristicHandbookDict, on_delete=models.CASCADE)
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    unit_id = models.ForeignKey(UnitDict, on_delete=models.CASCADE, null=True, blank=True)
    field_type = models.CharField(max_length=55, choices=CHOICE_FIELDS_TYPE, default=FIELDS_TEXT)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'characteristic_attributes'


class CharacteristicProduct(models.Model):
    """ Characteristic products models """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    attribute_id = models.ForeignKey(CharacteristicHandbookDict, on_delete=models.CASCADE)
    value = models.ForeignKey(CharacteristicAttributes, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.product_id} - {self.attribute_id} - {self.value}'

    class Meta:
        db_table = 'characteristic_products'
