from django.contrib import admin
from common.clients.categories.categories import CategoryModel
from common.clients.sliders.main_sliders import MainCarouselModel
from common.seller.seller import SellerModel
from common.clients.brand.brand import BrandModel
from common.auth.auth import User
from common.clients.access.access import AccessRole, UserRole, ModuleAccess
from common.clients.modules.modules import ClientModule


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone', 'first_name', 'last_name', 'is_active', 'date_joined')


@admin.register(AccessRole)
class AccessRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'role', 'code_role')


@admin.register(UserRole)
class UserRoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'role')


@admin.register(ClientModule)
class ClientModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name')


@admin.register(ModuleAccess)
class ClientModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'role', 'can_access', 'can_change', 'can_remove')


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
