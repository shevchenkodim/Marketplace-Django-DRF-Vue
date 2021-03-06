from syms_marketplace import settings
from common.dictionaries.dictionaries import CurrencyDict
from common.products.categories.categories import CategoryModel
from common.cart.cart import Cart


def client_data_context(request):
    cart_obj = Cart(request)

    context = dict()
    context["CART"] = cart_obj.get_cart_json(request)
    context["DEBUG"] = settings.DEBUG
    context["categories_list"] = CategoryModel.objects.all().select_related('icon')
    context["main_currency"] = CurrencyDict.objects.get_or_create(code='UAH', value='грн')[0].value
    return context
