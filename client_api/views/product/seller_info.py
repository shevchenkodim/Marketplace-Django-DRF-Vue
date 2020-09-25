from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only
from common.products.product.product import Product
from common.seller.seller import SellerModel


@api_view(['GET'])
@client_or_none_only
def get_seller_info_by_product(request, slug_p):
    data = dict()
    state = dict()
    try:
        product = Product.objects.get(product_id=slug_p)
        seller = SellerModel.objects.get(id=product.seller_id.id)
        data["name"] = seller.name
        data["logo"] = seller.image_logo.url
        data["absolute_url"] = seller.get_absolute_url()
        data["phone"] = seller.phone
        data["email"] = seller.email
        data["address"] = seller.address
    except Product.DoesNotExist:
        data = {"errors": {"message": "Такого продукта немає"}}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    return Response({"data": data, "state": state}, status=status.HTTP_200_OK)
