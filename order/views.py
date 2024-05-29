from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart
from .models import Order, OrderDetail


def order_create(request):
    if request.method == 'POST':
        cart_items = Cart.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        address = request.POST['address']

        order, created = Order.objects.get_or_create(user=request.user, total=total_price, address=address)
        order.save()

        for item in cart_items:
            order_detail, created = OrderDetail.objects.get_or_create(order=order, product=item.product, quantity=item.quantity)
            order_detail.save()

        cart_items.delete()

        messages.success(request, 'Ваш заказ принят!')
        return redirect('home')
    else:
        return redirect('home')


def order_detail(request, order_id):
    order = Order.objects.get(user=request.user, id=order_id)
    detail = OrderDetail.objects.filter(order=order)
    total_price = sum(item.product.price * item.quantity for item in detail)
    return render(request, 'order/detail.html', {'detail': detail, 'order': order, 'total_price': total_price})


def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order/orders.html', {"orders": orders})
