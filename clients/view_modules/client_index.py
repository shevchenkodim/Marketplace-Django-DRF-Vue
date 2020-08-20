import re
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST

# create client model
# from sf_common.models.application.client_model import Client
from clients import settings

from clients.view_modules.base import ModuleException, AppModule
from clients.view_modules.index.index_view import IndexView

url_start = settings.URL_CLIENT

# Need add load function caategories/user right menu


class ClientView:

    def __init__(self):
        self.app_module = AppModule()
        self.index_view = IndexView()

    def view_by_module(self, module):
        view = None
        if module == 'index':
            view = self.index_view
        return view

    def client_api(self, request):
        page_data = dict()
        (page_data, status) = self.do_request(request, page_data, True)
        response = Response(page_data, status=status)
        return response

    def client_index(self, request):
        page_data = dict()
        return self.do_request(request, page_data, False)

    def do_request(self, request, page_data, is_api=False):
        module = request.path.replace(url_start, '')
        module_data = dict()

        client_obj = request.session["client"]
        client_id = client_obj.get("client_id", 0)
        client = Client.objects.get(id=client_id)
        client.load_roles()
        template = None

        if len(module) > 0:
            if is_api and module[:4] == "/api":
                module = module[4:]
            if module[:1] == "/":
                module = module[1:]
            if module.find("/") > 0:
                module = module[:module.find("/")]
            access, client_module = self.app_module.access_module(client, module)
            if access.get("can_access") and client_module:
                view = self.view_by_module(module)
                try:
                    if is_api:
                        matches = re.search(r"\/c\/api\/" + module + "\/(?P<command>.*)(\?w+)?", request.path)
                        if matches:
                            command = matches["command"]
                        (module_data, status) = view.do_api(request, client, access, command=command)
                    else:
                        (module_data, template) = view.do(request, client, access)
                    if 'redirect' in module_data:
                        return redirect(module_data.get("redirect"))
                except ModuleException:
                    add_data = {"error": {"code": 500, "message": "Server Error"}}
                    return render(request, '500.html', {**page_data, **add_data})
            else:
                add_data = {"error": {"code": 403, "message": "Access denied"}}
                return render(request, '403.html', {**page_data, **add_data})

        page_data = {**module_data, **page_data}
        if is_api:
            return page_data, status
        else:
            return render(request, (template if template else 'base.html'), page_data)
