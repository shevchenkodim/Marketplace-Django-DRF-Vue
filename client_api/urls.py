from django.urls import path, include
from client_api.views.novelty.novelties import NoveltiesView

app_name = 'client_api'
urlpatterns = [
    path('auth/', include('client_api.auth.urls')),

    path('novelties', NoveltiesView.as_view(), name='novelties'),
]
