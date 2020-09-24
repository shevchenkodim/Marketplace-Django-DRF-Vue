from django.db import models
from common.dictionaries.dictionaries import SellerBlockDict
from common.front_tools.front_tools import CustomizationOfAppearance
from common.seller.seller import SellerModel


class SellerBlockInfo(CustomizationOfAppearance):
    block = models.ForeignKey(SellerBlockDict, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    order_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'seller_block_info'
        ordering = ['order_id']

    def __str__(self):
        return f"{self.block.code}, {self.seller_id.name}"


class SellerBlockItems(models.Model):
    seller_block_info = models.ForeignKey(SellerBlockInfo, on_delete=models.CASCADE)
