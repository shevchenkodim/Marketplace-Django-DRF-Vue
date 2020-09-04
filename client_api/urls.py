from django.urls import path

from client_api.views.novelty.novelties import NoveltiesView

app_name = 'client_api'
urlpatterns = [
    path('novelties', NoveltiesView.as_view(), name='novelties'),
]
