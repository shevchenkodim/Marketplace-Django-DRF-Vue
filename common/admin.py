from django.contrib import admin
from common.clients.categories.categories import CategoryModel
from common.clients.sliders.main_sliders import MainCarouselModel
from common.seller.seller import SellerModel
from common.clients.brand.brand import BrandModel


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name', 'slug', 'is_active')


@admin.register(MainCarouselModel)
class MainCarouselModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'item_alt', 'item_image')


@admin.register(SellerModel)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name', 'slug')


@admin.register(BrandModel)
class BrandModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name')
