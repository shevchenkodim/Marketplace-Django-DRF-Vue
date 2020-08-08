from django.urls import path
from clients.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='clients_index')
]