from django.core.exceptions import ValidationError

from common.access.access import AccessRole
from common.clients.access.access import ModuleAccess, ClientModule
from common.models import User


class AppModule(object):
    class FieldNotFilledException(ValidationError):
        def __init__(self, message, field):
            super(ValidationError, self).__init__(message)
            self.field = field

    class FieldFormatNotMatching(Exception):
        def __init__(self, message, field):
            super(ValidationError, self).__init__(message)
            self.field = field

    def check_field(self, value, min_length, max_length, field):
        if len(value) < min_length or len(value) > max_length:
            raise self.FieldFormatNotMatching("Field not filled", field)

    def access_module(self, client, module_name):

        if client:
            user_roles = User.user_roles(client.id)
        else:
            user_roles = set(AccessRole.objects.get(code_role='new_client'))

        try:
            client_module = ClientModule.objects.get(code=module_name)
        except ClientModule.DoesNotExist:
            client_module = None
        module_access = ModuleAccess.objects.filter(module__code=module_name, role__in=user_roles)
        access = {"can_access": False, "can_change": False, "can_remove": False}
        for module in module_access:
            if module.can_access:
                access["can_access"] = True
            if module.can_change:
                access["can_change"] = True
            if module.can_remove:
                access["can_remove"] = True

        return access, client_module

    def do_api(self, request, client, access, command):
        for method in self.api_methods:
            if method.get("command") == command and method.get("method"):
                return method.get("method")(request, client, access)

    def __init__(self):
        self.api_methods = []
        self.module_name = ""


class ModuleException(Exception):
    pass
