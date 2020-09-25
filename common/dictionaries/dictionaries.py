from common.dictionaries.base import Dictionaries
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


class IconDict(Dictionaries):
    """ Icon dict model """

    class Meta:
        db_table = 'dict_icon'


class CurrencyDict(Dictionaries):
    """ Currency dict model """

    class Meta:
        db_table = 'dict_currency'


class UnitDict(Dictionaries):
    """ Units dict model """

    class Meta:
        db_table = 'dict_unit'


class BrandDict(Dictionaries):
    """ Product brand dict model """
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'dict_brand'
        ordering = ['value']
