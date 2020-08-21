from django.db import models
from common.access.access import ItemAccess


class ClientModule(models.Model):
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}|{self.name}"

    class Meta:
        db_table = "clients_module"


class ModuleAccess(ItemAccess):
    module = models.ForeignKey(ClientModule, on_delete=models.CASCADE, verbose_name='Модуль')

    class Meta:
        db_table = 'client_access_module'
