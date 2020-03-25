from django.urls import path
from . import views
app_name = 'category'
urlpatterns = [
    path('category/index/', views.index, name='index'),
    path('category/create/', views.create, name='create'),
    path('category/edit/<int:pk>', views.edit, name='edit'),
    path('category/delete/<int:pk>', views.delete, name='delete'),
]

