from django.db import models
from django.conf import settings
from common.products.product.product import Product


class CartItems(models.Model):
    """ Model for items in client cart """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Клієнт')
    count = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.product.__str__()}"

    def get_item_json(self):
        return {"product_id": self.product.product_id, "quantity": self.count, "price": str(self.product.price)}

    @staticmethod
    def client_has_cart_item(product_id, client):
        return CartItems.objects.filter(product__product_id=product_id, client=client).exists()

    @staticmethod
    def get_len_items(client):
        return CartItems.objects.filter(client=client).count()
