from django.db import models


class Dictionaries(models.Model):
    code = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255, unique=True)

    class Meta:
        abstract = True
