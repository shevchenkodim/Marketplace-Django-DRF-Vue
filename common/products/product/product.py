from django.db import models
from django.urls import reverse

from common.dictionaries.dictionaries import BrandDict
from common.products.categories.categories import CategoryModel
from common.seller.seller import SellerModel
from common.seo.seo import SeoModel


class Product(SeoModel):
    """ Product model """
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, unique=True)
    product_id = models.CharField(max_length=55, unique=True, db_index=True)
    is_available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    old_price = models.DecimalField(max_digits=15, decimal_places=2)
    is_active = models.BooleanField(default=True)
    quantity = models.IntegerField(default=0)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    seller_id = models.ForeignKey(SellerModel, on_delete=models.CASCADE)
    brand = models.ForeignKey(BrandDict, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'product'
        ordering = ['created_at']

    def __str__(self):
        return self.product_id

    def get_absolute_url(self):
        return reverse('client:product_index',
                       kwargs={'slug_c': self.category_id.code_name, 'slug_p': self.product_id})

    def save(self, *args, **kwargs):
        if not self.product_id:
            self.product_id = generate_product_id()
        super(Product, self).save(*args, **kwargs)


def generate_product_id():
    """ Generate new product_id on create """
    last_product = Product.objects.all().order_by('created_at').last()
    last_value = last_product.product_id if last_product else '0000000000'
    value_int = int(last_value) + 1
    value_len = len(str(value_int))
    return last_value[:-value_len] + str(value_int)
