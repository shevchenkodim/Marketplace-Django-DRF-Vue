from django.db import models


class MainCarouselModel(models.Model):
    order_id = models.IntegerField(default=0)
    item_alt = models.CharField(max_length=100, blank=True)
    item_image = models.ImageField(upload_to='slider_main')

    class Meta:
        db_table = 'client_main_carousel'
        ordering = ['order_id']
