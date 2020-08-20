from django.views.generic import TemplateView
from common.clients.sliders.main_sliders import MainCarouselModel
from common.clients.categories.categories import CategoryModel


class IndexView(TemplateView):
    """Index page"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_carousel_items"] = MainCarouselModel.objects.all()
        return context


class ProductsForCategoriesView(TemplateView):
    """Product for categories page"""
    template_name = "products_for_categories/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = CategoryModel.objects.get(slug=self.kwargs['slug_c'])
        return context


class ProductView(TemplateView):
    """Product page"""
    template_name = "product/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["product"] = 'Product test'
        return context
