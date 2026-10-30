from django.shortcuts import render

from .models import Dish


def home(request):
    dishes = Dish.objects.filter(is_available=True).select_related('category')
    return render(request, 'menu/home.html', {'dishes': dishes})
