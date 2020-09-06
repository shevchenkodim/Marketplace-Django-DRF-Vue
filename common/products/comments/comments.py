from common.products.product.product import Product
from django.conf import settings
from django.db import models
from django.db.models import Avg


class ProductComment(models.Model):
    """ Product comment model """
    owner_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    likes_count = models.IntegerField(default=0)
    dislikes_count = models.IntegerField(default=0)
    rating_stars = models.IntegerField(default=0)
    date_time_add = models.DateTimeField(auto_now_add=True)
    reply_to = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        db_table = 'product_comment'
        ordering = ['date_time_add']

    @staticmethod
    def get_comment_count(product):
        """ Get comment count for product """
        return ProductComment.objects.filter(product_id__product_id=product.product_id).count()

    @staticmethod
    def get_average_star_rating(product):
        """ Get average star rating for product """
        result = ProductComment.objects.filter(product_id__product_id=product.product_id).aggregate(Avg('rating_stars'))
        result_number = 0
        if result.get('rating_stars__avg'):
            result_number = int(result.get('rating_stars__avg'))
        return result_number
