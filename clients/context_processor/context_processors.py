from common.categories.categories import CategoryModel


def client_data_context(request):
    context = dict()
    context["categories_list"] = CategoryModel.objects.all()
    return context
