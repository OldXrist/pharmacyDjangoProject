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
    cart_items = Cart.objects.filter(user=request.user)
    order = Order.objects.filter(user=request.user)[0]
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'order.html', {'cart_items': cart_items, 'total_price': total_price, 'order': order})