from django.views.generic import TemplateView
from common.categories.categories import CategoryModel


class IndexView(TemplateView):
    """Index page"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories_list"] = CategoryModel.objects.all()
        return context
