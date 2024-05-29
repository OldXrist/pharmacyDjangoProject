from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart
from order.models import Order, OrderDetail
from shop.models import Wishlist
from .models import UserDetail
from django.contrib.auth.models import User


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


def info_update(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        address = request.POST['address']
        city = request.POST['city']
        phone = request.POST['phone']
        email = request.POST['email']

        user = User.objects.get(id=request.user.id)
        user_detail = UserDetail.objects.get(user=request.user)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email

        user_detail.address = address
        user_detail.city = city
        user_detail.phone = phone

        user.save()
        user_detail.save()
        return redirect('account')
    else:
        return redirect('account')

