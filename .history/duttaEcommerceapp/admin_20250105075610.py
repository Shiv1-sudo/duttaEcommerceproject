'''from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from duttaEcommerceapp.models.models import User

# Register your models here.


class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Register the new UserAdmin
admin.site.register(User, UserAdmin)

# Unregister the Group model from admin since we're not using it
admin.site.unregister(Group)

'''
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from duttaEcommerceapp.models.models import User
from duttaEcommerceapp.models.product import Category, SubCategory, Product

class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone_number', 'address')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    filter_horizontal = ()

# Register the new UserAdmin
admin.site.register(User, UserAdmin)

# Unregister the Group model from admin since we're not using it
admin.site.unregister(Group)

# Register additional models for product management
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_group', 'category')
    search_fields = ('name', 'age_group', 'category__name')
    ordering = ('category', 'name')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'subcategory', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'subcategory__name')
    list_filter = ('subcategory', 'price', 'created_at')
    ordering = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
