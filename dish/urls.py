from django.urls.conf import path
from . import views
app_name = 'dish'
urlpatterns = [
    path('dish/index', views.index, name='index'),
    path('dish/create', views.create, name='create'),
    path('dish/edit/<int:pk>', views.edit, name='edit'),
    path('dish/delete/<int:pk>', views.delete, name='delete'),
]

