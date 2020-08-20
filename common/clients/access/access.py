from django.db import models
from django.contrib.auth.models import User

from common.clients.modules.modules import ClientModule


class AccessRole(models.Model):
    role = models.CharField(max_length=40, verbose_name=_('Назва ролі'))
    code_role = models.CharField(max_length=40, unique=True, verbose_name=_('Код ролі'))

    def __str__(self):
        return f"{self.role}"

    class Meta:
        db_table = 'access_role'


class UserRole(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Користувач'))
    role = models.ForeignKey(AccessRole, on_delete=models.CASCADE, verbose_name=_('Роль'))

    def __str__(self):
        return f"{self.user} - {self.role}"

    class Meta:
        db_table = 'client_user_role'


class ItemAccess(models.Model):
    role = models.ForeignKey(AccessRole, on_delete=models.CASCADE, verbose_name=_('Роль'))
    can_access = models.BooleanField(default=True, verbose_name=_('Може читати'))
    can_change = models.BooleanField(default=False, verbose_name=_('Може змінювати'))
    can_remove = models.BooleanField(default=False, verbose_name=_('Може видаляти'))

    def access_json(self):
        return {"role_id": self.role.id, "can_access": self.can_access, "can_change": self.can_change, "can_remove": self.can_remove}

    class Meta:
        abstract = True


class ModuleAccess(ItemAccess):
    module = models.ForeignKey(ClientModule, on_delete=models.CASCADE, verbose_name=_('Модуль'))

    class Meta:
        db_table = 'client_access_module'
