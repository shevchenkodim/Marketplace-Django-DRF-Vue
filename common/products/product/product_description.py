from django.db import models
from common.products.product.product import Product


class ProductDescription(models.Model):
    """ Product description model """
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    order_id = models.IntegerField(default=0)

    class Meta:
        db_table = 'product_description'
        ordering = ['order_id']

    def __str__(self):
        return self.title

    @staticmethod
    def get_description_by_product(product_id):
        return [{"title": description.title, "description": description.description} for description in
                ProductDescription.objects.filter(product_id__id=product_id)]
