from django.shortcuts import render, redirect
from django.contrib import messages
from cart.models import Cart
from order.models import Order, OrderDetail
from shop.models import Wishlist
from .models import UserDetail


def account(request):
    pass