from django.urls import path
from client_api.auth.auth import client_sign_in, client_sign_up

urlpatterns = [
    path('sign_in', client_sign_in, name='sign_in'),
    path('sign_up', client_sign_up, name='sign_up'),
]
