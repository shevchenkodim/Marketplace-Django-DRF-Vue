from common.dictionaries.base import Dictionaries
from common.products.categories.categories import CategoryModel
from django.db import models


class TextSizeDict(Dictionaries):
    """ Text size dict model """

    class Meta:
        db_table = 'dict_size_colors'


class TextColorDict(Dictionaries):
    """ Text color dict model """

    class Meta:
        db_table = 'dict_text_colors'


class BackgroundColorDict(Dictionaries):
    """ Background color dict model """

    class Meta:
        db_table = 'dict_background_colors'


class SellerBlockDict(Dictionaries):
    """ Seller block dict model """

    class Meta:
        db_table = 'dict_seller_block'


class IconDict(Dictionaries):
    """ Icon dict model """

    class Meta:
        db_table = 'dict_icon'


class SellerBlockItemDict(Dictionaries):
    """ Item seller block dict model """
    block_id = models.ForeignKey(SellerBlockDict, on_delete=models.CASCADE)
    icon = models.ForeignKey(IconDict, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dict_seller_block_item'


class CurrencyDict(Dictionaries):
    """ Currency dict model """

    class Meta:
        db_table = 'dict_currency'


class UnitDict(Dictionaries):
    """ Units dict model """

    class Meta:
        db_table = 'dict_unit'


class CharacteristicHandbookDict(Dictionaries):
    """ Characteristic handbook dict model """
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)

    class Meta:
        db_table = 'dict_characteristic_handbook'


class BrandDict(Dictionaries):
    """ Product brand dict model """
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dict_brand'
        ordering = ['value']
