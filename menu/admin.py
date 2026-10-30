from django.contrib import admin

from .models import Category, Dish, Review

admin.site.register(Category)
admin.site.register(Review)


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available']
    list_filter = ['category', 'is_available']
    search_fields = ['name']
