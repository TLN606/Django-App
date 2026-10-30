from django.db.models import Prefetch
from django.shortcuts import render

from .models import Category, Dish


# Hình tô theo tên danh mục; danh mục mới thì lần lượt dùng các hình còn lại.
GLYPHS = {'cơm': 'com', 'bún - phở': 'bun', 'ăn vặt': 'anvat', 'đồ uống': 'douong'}
FALLBACK = ['com', 'bun', 'anvat', 'douong']


def home(request):
    categories = Category.objects.prefetch_related(
        Prefetch('dishes', queryset=Dish.objects.filter(is_available=True), to_attr='available_dishes')
    )
    # Danh mục không còn món nào đang bán thì không hiện.
    categories = [c for c in categories if c.available_dishes]
    # Thứ tự bữa trưa: Cơm trước; danh mục lạ xếp sau theo tên.
    order = list(GLYPHS)
    categories.sort(key=lambda c: order.index(c.name.lower()) if c.name.lower() in order else len(order))
    for i, c in enumerate(categories):
        c.glyph = GLYPHS.get(c.name.lower(), FALLBACK[i % len(FALLBACK)])
    return render(request, 'menu/home.html', {'categories': categories})
