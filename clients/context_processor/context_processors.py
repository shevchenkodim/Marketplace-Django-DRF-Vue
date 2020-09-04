from Marketplace_Django_DRF_Vue import settings
from common.products.categories.categories import CategoryModel


def client_data_context(request):
    context = dict()
    context["DEBUG"] = settings.DEBUG
    context["categories_list"] = CategoryModel.objects.all()
    return context
