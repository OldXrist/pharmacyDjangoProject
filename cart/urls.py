from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart_page, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('add/<int:product_id>/', views.cart_add, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
]
