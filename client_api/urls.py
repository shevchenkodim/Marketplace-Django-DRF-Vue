from django.urls import path
from client_api.auth.auth import client_sign_in, client_sign_up
from client_api.views.novelty.novelties import NoveltiesView

app_name = 'client_api'
urlpatterns = [
    path('signin', client_sign_in, 'sign_in'),
    path('signup', client_sign_up, 'sign_up'),

    path('novelties', NoveltiesView.as_view(), name='novelties'),
]
