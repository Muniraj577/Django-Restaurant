from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm


# Create your views here.


def index(request):
    category = Category.objects.all()
    context = {'category': category, 'category_index': 'active'}
    return render(request, 'category/index.html', context)


def create(request):
    form = CategoryForm()
    if request.method == 'GET':
        return render(request, 'category/create.html', {'form': form, 'category_index': 'active'})
    elif request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('category:index')


def edit(request, pk=id):
    if request.method == 'GET':
        category = Category.objects.get(pk=pk)
        form = CategoryForm(instance=category)
        return render(request, 'category/edit.html', {'category': category, 'form': form, 'category_index': 'active'})
    elif request.method == 'POST':
        category = Category.objects.get(pk=pk)
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category:index')
        return render(request, 'category/edit.html', {'category': category, 'category_index': 'active'})


def delete(request, pk=id):
    category = Category.objects.get(pk=pk)
    category.delete()
    return redirect('category:index')

