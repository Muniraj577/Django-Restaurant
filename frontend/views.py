from django.shortcuts import render, get_object_or_404, redirect
from Category.models import Category
from dish.models import Dish
from django.contrib import messages
from cart.forms import CartAddDishForm


# Create your views here.


def index(request):
    categories = Category.objects.all()
    dishes = Dish.objects.all()
    context = {
        'categories': categories,
        'dishes': dishes
    }
    return render(request, 'frontend/index.html', context)


# def detail(request, pk=id):
#     try:
#         dish = Dish.objects.get(pk=pk)
#         cart_dish_form = CartAddDishForm()
#     except Dish.DoesNotExist:
#         messages.error("Dish doesn't exist.")
#         return redirect('frontend:index')
#     return render(request, 'frontend/detail.html', context={'dish': dish, 'cart_dish_form': cart_dish_form})

def detail(request, pk=id):
    dish = Dish.objects.get(pk=pk)
    cart_dish_form = CartAddDishForm()
    context = {
        'dish': dish,
        'cart_dish_form': cart_dish_form
    }
    return render(request, 'frontend/detail.html', context)