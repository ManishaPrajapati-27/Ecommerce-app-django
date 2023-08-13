from django.urls import path
from cart.views import add_to_cart, cart, remove_cart, remove_coupon

urlpatterns = [
    path("", cart, name="cart"),
    path("add-to-cart/<uid>", add_to_cart, name="add_to_cart"),
    path("remove-cart/<cart_item_uid>", remove_cart, name="remove_cart"),
    path("remove-coupon/<cart_id>", remove_coupon, name="remove_coupon"),
]
