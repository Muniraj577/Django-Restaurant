from django.urls import path
from . import views

app_name = 'checkout'

urlpatterns = [
    path('checkout/create/', views.order_create, name='order_create'),
    path('admin/orders/index', views.index, name='index'),
]
