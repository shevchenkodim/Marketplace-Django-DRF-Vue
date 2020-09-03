from django.db import models

from common.dictionaries.dictionaries import BrandDict
from common.products.categories.categories import CategoryModel
from common.seller.seller import SellerModel
from common.seo.seo import SeoModel


class Product(SeoModel):
    """ Product model """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    product_id = models.CharField(max_length=55, unique=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField(default=True)
    quantity = models.ImageField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandDict, on_delete=models.CASCADE)

    # def get_sale_prace(self):
    #     return ''
    #
    # def get_absolute_url(self):
    #     return ''

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'product'
