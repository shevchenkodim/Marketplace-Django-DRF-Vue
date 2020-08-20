from rest_framework.status import HTTP_200_OK
from clients.view_modules.base import AppModule


class IndexView(AppModule):

    def do(self, request, client, access):
        page_data = {"page_title": "Index page"}
        return page_data, 'main/index.html'

    def do_api(self, request, client, access, command):
        page_data = dict()
        if command == "init" and request.method == "POST":
            page_data["result"] = ''

        return page_data, HTTP_200_OK
