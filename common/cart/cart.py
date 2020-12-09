from decimal import Decimal
from common.models import User
from django.conf import settings
from common.cart.cart_items import CartItems
from common.products.product.product import Product


class Cart(object):

    def __init__(self, request):
        """ Initialize the cart """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart
        if request.user and request.user.id:
            if 'client' in request.user.user_roles(request.user.id):
                self.__synchronization_database_with_cart(request)

    def __synchronization_database_with_cart(self, request):
        cart_items = CartItems.objects.filter(client=request.user)
        for item in cart_items:
            _ = item.get_item_json()
            self.__add_item_to_session(request, _)
        # for item in self.cart:
        #     count = self.cart[item]["quantity"]
        #     self.__add_item_to_database(request, item, count)

    def add_item(self, request, product):
        """  Add a product to the cart"""
        if request.user and request.user.id:
            if 'client' in request.user.user_roles(request.user.id):
                self.__add_item_to_database(request, product)
        self.__add_item_to_session(request, product)

    def __add_item_to_session(self, request, product):
        """  Add a product to the cart or update its quantity """
        product_id = product["product_id"]
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': product["quantity"], 'price': product["price"]}
        self.cart[product_id]['quantity'] = product["quantity"]
        self.save_session()

    def __add_item_to_database(self, request, product, count):
        """  Add a product to the database cart or update its quantity """
        if not CartItems.client_has_cart_item(product, request.user):
            CartItems.objects.create(
                product__product_id=product,
                client=request.user,
                count=count
            )

    def save_session(self):
        self.session.modified = True

    def get_len(self, request):
        if request.user and request.user.id:
            if 'client' in request.user.user_roles(request.user.id):
                return CartItems.get_len_items(request.user)
            else:
                return len(self.cart)
        else:
            return len(self.cart)


# def __init__(self, request):
#     """ Initialize the cart """
#     self.session = request.session
#     cart = self.session.get(settings.CART_SESSION_ID)
#     if not cart:
#         cart = self.session[settings.CART_SESSION_ID] = {}
#     self.cart = cart


#
# def remove(self, product):
#     """ Remove a product from the cart """
#     product_id = str(product.product_id)
#     if product_id in self.cart:
#         del self.cart[product_id]
#         self.save()

# def __iter__(self):
#     """ Iterate over the items in the cart and get the products from the database """
#     product_ids = self.cart.keys()
#     products = Product.objects.filter(product_id__in=product_ids)
#
#     cart = self.cart.copy()
#     for product in products:
#         cart[str(product.product_id)]['product'] = product
#
#     for item in cart.values():
#         item['price'] = Decimal(item['price'])
#         item['total_price'] = item['price'] * item['quantity']
#         yield item
#
# def __len__(self):
#     """ Count all items in the cart """
#     return sum(item['quantity'] for item in self.cart.values())
#
# def get_total_price(self):
#     """ Return total price in the cart """
#     return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())
#
# def clear(self):
#     """ Remove cart from session """
#     del self.session[settings.CART_SESSION_ID]
#     self.save()
