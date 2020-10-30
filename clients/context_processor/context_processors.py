from Marketplace_Django_DRF_Vue import settings
from common.dictionaries.dictionaries import CurrencyDict
from common.products.categories.categories import CategoryModel


def client_data_context(request):
    context = dict()
    context["DEBUG"] = settings.DEBUG
    context["categories_list"] = CategoryModel.objects.all().select_related('icon')
    context["main_currency"] = CurrencyDict.objects.get_or_create(code='UAH', value='грн')[0].value
    return context
