from django.contrib import admin
from common.products.categories.categories import CategoryModel
from common.clients.sliders.main_sliders import MainCarouselModel
from common.products.characteristic.characteristic import CharacteristicAttributes, CharacteristicProduct
from common.products.comments.comments import ProductComment
from common.products.product.product import Product
from common.products.product.product_image import ProductImage
from common.seller.seller import SellerModel
from common.models import User
from common.access.access import AccessRole, UserRole
from common.dictionaries.dictionaries import BrandDict, UnitDict, CharacteristicHandbookDict, CurrencyDict


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code')


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner_id', 'text', 'likes_count', 'dislikes_count', 'rating_stars', 'date_time_add')


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'item_alt', 'product_id')


@admin.register(UnitDict)
class UnitDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')


@admin.register(CharacteristicHandbookDict)
class CharacteristicHandbookDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code', 'category_id')


@admin.register(CharacteristicAttributes)
class CharacteristicAttributesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'field_type')


@admin.register(CharacteristicProduct)
class CharacteristicProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'product_id', 'attribute_id')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'date_joined')


@admin.register(AccessRole)
class AccessRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'code_role')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')


@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name', 'slug', 'is_active')


@admin.register(MainCarouselModel)
class MainCarouselModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_id', 'item_alt', 'item_image')


@admin.register(SellerModel)
class SellerModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'code_name', 'slug')


@admin.register(BrandDict)
class BrandDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')


@admin.register(CurrencyDict)
class CurrencyDictAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'code')
