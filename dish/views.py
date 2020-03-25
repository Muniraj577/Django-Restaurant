from django.shortcuts import render, redirect
from .forms import DishForm
from .models import Dish
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def index(request):
    dish = Dish.objects.all()
    return render(request, 'dish/index.html', {'dish': dish, 'dish_index': 'active'})


def create(request):
    form = DishForm()
    if request.method == 'GET':
        return render(request, 'dish/create.html', {'form': form, 'dish_index': 'active'})
    elif request.method == 'POST':
        form = DishForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dish:index')
        return render(request, 'dish/create.html', {'form': form, 'dish_index': 'active'})


def edit(request, pk=id):
    if request.method == 'GET':
        dish = Dish.objects.get(pk=pk)
        form = DishForm(instance=dish)
        return render(request, 'dish/edit.html', {'form': form, 'dish': dish, 'dish_index': 'active'})
    elif request.method == 'POST':
        dish = Dish.objects.get(pk=pk)
        form = DishForm(request.POST, request.FILES, instance=dish)
        if form.is_valid():
            form.save()
            return redirect('dish:index')
        return render(request, 'dish/edit.html', {'dish': dish, 'dish_index': 'active'})


def delete(request, pk=id):
    dish = Dish.objects.get(pk=pk)
    dish.delete()
    return redirect('dish:index')
