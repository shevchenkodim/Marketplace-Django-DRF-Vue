from django.db import models
from common.seo.seo import SeoModel
from mptt.models import MPTTModel, TreeForeignKey


class CategoryModel(MPTTModel, SeoModel):
    name = models.CharField(max_length=100, unique=True, db_index=True)
    code_name = models.CharField(max_length=100, unique=True, db_index=True)
    slug = models.SlugField(max_length=125, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    icon = models.CharField(max_length=50, blank=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    # @models.permalink
    # def get_absolute_url(self):
    #     return ('catalog_category', (), {'category_slug': self.slug})

    class MPTTMeta:
        class Meta:
            db_table = 'categories'
            ordering = ['-created_at']
