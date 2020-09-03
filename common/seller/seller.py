from django.db import models
from django.urls import reverse

from common.seo.seo import SeoModel


class SellerModel(SeoModel):
    """ Seller model """
    name = models.CharField(max_length=125, unique=True, db_index=True)
    code_name = models.CharField(max_length=125, unique=True, db_index=True)
    slug = models.SlugField(max_length=125, unique=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def get_absolute_url(self):
    #     return reverse('client:products_for_category_index', kwargs={'slug_c': self.slug})

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'seller'
        ordering = ['name']
