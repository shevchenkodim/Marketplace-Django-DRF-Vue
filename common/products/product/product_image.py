from django.db import models
from common.products.product.product import Product


class ProductImage(models.Model):
    """ Product image model """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'product/{product_id}/image')
    item_alt = models.CharField(max_length=100, blank=True)
    order_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_image'
        ordering = ['order_id']

    def __str__(self):
        return self.image

    # def get_absolute_url(self):
    #     return ''
