from django.urls import path, include
from client_api.views.novelty.novelties import NoveltiesView
from client_api.auth.auth import client_auth, client_auth_init
from client_api.views.product.product_comment import get_comments_by_product
from client_api.views.product.product_info import get_product_info
from client_api.views.product.seller_info import get_seller_info_by_product

app_name = 'client_api'
urlpatterns = [
    # auth
    path('auth/', client_auth, name='auth'),
    path('auth/init', client_auth_init, name='auth_init'),

    # main page
    path('novelties', NoveltiesView.as_view(), name='novelties'),

    # product page
    path('product/<slug:slug_p>', get_product_info, name='get_product_info'),
    path('seller/<slug:slug_p>', get_seller_info_by_product, name='get_seller_info'),
    path('comments/<slug:slug_p>', get_comments_by_product, name='get_comments'),
]
