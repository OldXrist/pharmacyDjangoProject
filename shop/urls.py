from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop_page, name='shop'),
    path('product/<product_id>', views.product_details, name='product-details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('category/<int:category_id>/', views.shop_by_category, name='shop_by_category'),
    path('add/<int:product_id>/', views.wishlist_add, name='add_to_wishlist'),
    path('remove/<int:item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
