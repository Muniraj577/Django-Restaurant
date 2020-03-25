from django.shortcuts import render, get_object_or_404
from Category.models import Category
from dish.models import Dish


# Create your views here.


def index(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    context = {
        'categories': categories,
        'dishes': dishes
    }
    return render(request, 'frontend/index.html', context)
