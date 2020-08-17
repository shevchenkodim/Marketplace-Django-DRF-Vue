from django.db import models


class BrandModel(models.Model):
    name = models.CharField(max_length=125, unique=True, db_index=True)
    code_name = models.CharField(max_length=125, unique=True, db_index=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'brand'
        ordering = ['name']
