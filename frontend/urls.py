from django.urls.conf import path
from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.index, name='index'),
    path('dish/detail/<int:pk>', views.detail, name='detail'),
]
