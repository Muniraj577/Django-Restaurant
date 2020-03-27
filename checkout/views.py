from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart
from django.contrib.auth.models import User


def confirm(request):
    return render(request, 'checkout/confirm.html')


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        # user = User.objects.get(pk=pk)
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         dish=item['dish'],
                                         price=item['price'],
                                         quantity=item['quantity'])
            cart.clear()
            return render(request, 'checkout/confirm.html', {'order': order, 'cart': cart})
    else:
        form = OrderCreateForm()
        return render(request, 'checkout/checkout.html', {'cart': cart, 'form': form})
