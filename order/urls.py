from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('list/', views.order_list, name="order_list"),
    path('detail/<int:order_id>', views.order_detail, name="order_detail"),
]
