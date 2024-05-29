from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart
from order.models import Order, OrderDetail
from shop.models import Wishlist
from .models import UserDetail


def account(request):
    orders = Order.objects.filter(user=request.user)
    cart = Cart.objects.filter(user=request.user)
    details = UserDetail.objects.get(user=request.user)
    wishlist = Wishlist.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart)

    context = {
        "orders": orders,
        "cart": cart,
        "details": details,
        "total_price": total_price,
        "wishlist": wishlist,
    }

    return render(request, 'user/account.html', context)
