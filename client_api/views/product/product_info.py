from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from clients.utils.decorators import client_or_none_only
from common.products.characteristic.characteristic import CharacteristicProduct
from common.products.comments.comments import ProductComment
from common.products.product.product import Product
from common.products.product.product_description import ProductDescription
from common.products.product.product_image import ProductImage


@api_view(['GET'])
@client_or_none_only
def get_product_info(request, slug_p):
    data = dict()
    state = dict()
    try:
        product = Product.objects.get(product_id=slug_p)
        data["product_name"] = product.name
        data["product_id"] = product.product_id
        data["comment_count"] = ProductComment.get_comment_count(product)
        data["average_star_rating"] = ProductComment.get_average_star_rating(product)
        data["is_available"] = product.is_available
        data["price"] = product.price
        data["old_price"] = product.old_price
        data["product_images"] = ProductImage.get_images_by_product(product.product_id)
        data["product_descriptions"] = ProductDescription.get_description_by_product(product.product_id)
        data["characteristic_list"] = CharacteristicProduct.get_characteristic_by_product(product.product_id)
        data["short_character"] = product.short_character
    except Product.DoesNotExist:
        data = {"errors": {"message": "Такого продукта немає"}}
        return Response(data, status=status.HTTP_404_NOT_FOUND)
    return Response({"data": data, "state": state}, status=status.HTTP_200_OK)
