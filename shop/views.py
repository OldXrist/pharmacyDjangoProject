from django.shortcuts import render, redirect
from .models import Category, Product, Wishlist


def shop_page(request):
    category = Category.objects.all()
    products = Product.objects.filter(is_draft=False)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/shop.html', context)


def shop_by_category(request, category_id):
    category_name = Category.objects.get(id=category_id)
    search_category = Category.objects.all()
    products = Product.objects.filter(is_draft=False, category=category_id)
    context = {
        'category': search_category,
        'products': products,
        'cat_name': category_name
    }
    return render(request, 'shop/shop.html', context)


def product_details(request, product_id):
    product_details = Product.objects.get(id=product_id)
    ctg = Category.objects.get(name=product_details.category)
    related_products = Product.objects.filter(category=ctg)
    context = {
        'product': product_details,
        'related_products': related_products
    }
    return render(request, 'shop/product-details.html', context)


def wishlist(request):
    wishlist_items = Wishlist.objects.filter(user=request.user)
    return render(request, 'shop/wishlist.html', {'wishlist_items': wishlist_items})


def wishlist_add(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Wishlist.objects.get_or_create(product=product, user=request.user)
    cart_item.save()
    return redirect('wishlist')


def remove_from_wishlist(request, item_id):
    cart_item = Wishlist.objects.get(id=item_id)
    cart_item.delete()
    return redirect('wishlist')
