from django.db import models
from django.urls import reverse

from common.seo.seo import SeoModel


class SellerModel(SeoModel):
    """ Seller model """
    name = models.CharField(max_length=125, unique=True, db_index=True)
    code_name = models.CharField(max_length=125, unique=True, db_index=True)
    phone = models.CharField(max_length=20, unique=True, default='+380000000000')
    address = models.CharField(max_length=255, null=True, blank=True)
    schedule_work = models.TextField(blank=True)
    email = models.EmailField(default='default@gmail.com', unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image_logo = models.ImageField(upload_to='seller/logo', blank=True, null=True)

    class Meta:
        db_table = 'seller'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('client:seller_index', kwargs={'slug_s': self.code_name})

    def __str__(self):
        return self.name
