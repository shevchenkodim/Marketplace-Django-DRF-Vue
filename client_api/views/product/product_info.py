from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only
from common.products.product.product import Product


@api_view(['GET'])
@client_or_none_only
def get_product_info(request, slug_p):
    data = dict()
    state = dict()
    try:
        product = Product.objects.get(product_id=slug_p)
        data["product_name"] = product.name
    except Product.DoesNotExist:
        data = {"message": "Такого продукта немає"}
        return Response(data, status=status.HTTP_400_BAD_REQUEST)
    return Response({"data": data, "state": state}, status=status.HTTP_200_OK)
