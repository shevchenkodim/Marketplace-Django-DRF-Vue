from django.urls import path, include
from client_api.views.novelty.novelties import NoveltiesView
from client_api.auth.auth import client_auth, client_auth_init

app_name = 'client_api'
urlpatterns = [
    path('auth/', client_auth, name='auth'),
    path('auth/init', client_auth_init, name='auth_init'),

    path('novelties', NoveltiesView.as_view(), name='novelties'),
]
