from __future__ import absolute_import, unicode_literals

from django import forms
from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'modified_at')
    exclude = ('vote_score', 'num_vote_up', 'num_vote_down' )
    prepopulated_fields = {"slug": ("name",)}

    view_on_site = True

# class MyUserAdmin(AuthUserAdmin):
#     form = MyUserChangeForm
#     add_form = MyUserCreationForm
#     fieldsets = (
#             ('User Profile', {'fields': ('name',)}),
#     ) + AuthUserAdmin.fieldsets
#     list_display = ('username', 'name', 'is_superuser')
#     search_fields = ['name']
#
