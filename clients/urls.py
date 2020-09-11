from django.urls import path
from clients.views import IndexView, ProductsForCategoriesView, ProductView, client_logout


app_name = 'client'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('c/<slug:slug_c>', ProductsForCategoriesView.as_view(), name='products_for_category_index'),
    path('c/<slug:slug_c>/p/<slug:slug_p>', ProductView.as_view(), name='product_index'),
    path('u/logout', client_logout, name='client_logout'),
]
