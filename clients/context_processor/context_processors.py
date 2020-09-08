from Marketplace_Django_DRF_Vue import settings
from common.dictionaries.dictionaries import CurrencyDict
from common.products.categories.categories import CategoryModel


def client_data_context(request):
    context = dict()
    context["DEBUG"] = settings.DEBUG
    context["categories_list"] = CategoryModel.objects.all()
    context["main_currency"] = CurrencyDict.objects.get(code='UAH').value
    return context
