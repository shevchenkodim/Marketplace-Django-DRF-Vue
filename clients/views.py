from django.views.generic import TemplateView
from common.sliders.main_sliders import MainCarouselModel


class IndexView(TemplateView):
    """Index page"""
    template_name = "main/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["main_carousel_items"] = MainCarouselModel.objects.all()
        return context
