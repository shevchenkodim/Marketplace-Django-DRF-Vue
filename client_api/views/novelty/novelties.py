from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from common.products.product.product import Product
from common.products.product.product_image import ProductImage
from common.products.comments.comments import ProductComment


class NoveltiesView(APIView):
    """ This class need returns list novelty products """
    count = 8

    def get(self, request):
        response_list = []
        product_list = Product.objects.all()[:self.count]
        for product in product_list:
            resp_dict = dict()
            resp_dict["name"] = product.name
            resp_dict["code"] = product.code
            resp_dict["price"] = product.price
            resp_dict["old_price"] = product.old_price
            resp_dict["product_id"] = product.product_id
            resp_dict["product_url"] = product.get_absolute_url()
            resp_dict["is_available"] = product.is_available
            product_image = ProductImage.objects.filter(product_id__id=product.product_id).first()
            resp_dict["product_image"] = product_image.image.url
            resp_dict["comment_count"] = ProductComment.get_comment_count(product)
            resp_dict["average_star_rating"] = ProductComment.get_average_star_rating(product)
            response_list.append(resp_dict)
        return Response(data=response_list, status=status.HTTP_200_OK)
