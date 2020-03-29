from django.shortcuts import render
from .models import OrderItem, Order
from .forms import OrderCreateForm
from cart.cart import Cart
from dish.models import Dish


def index(request):
    order = Order.objects.all()
    dish = Dish.objects.all()
    order_items = OrderItem.objects.all()
    context = {
        'order': order,
        'dish': dish,
        'order_items': order_items,
        'order_index': 'active'
    }
    return render(request, 'checkout/index.html', context)


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
