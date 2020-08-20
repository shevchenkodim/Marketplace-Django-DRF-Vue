from django.db import models


class ClientModule(models.Model):
    code = models.CharField(max_length=40)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}|{self.name}"

    class Meta:
        db_table = "clients_module"
