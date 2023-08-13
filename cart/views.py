from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from products.models import Product, SizeVariant
from .models import Cart, CartItems, Coupon

# Create your views here.


def add_to_cart(request, uid):
    variant = request.GET.get("variant")

    # if variant:
    #     variant = request.GET.get('variant')

    product = Product.objects.get(uid=uid)
    user = request.user
    cart, _ = Cart.objects.get_or_create(user=user, is_paid=False)

    cart_item = CartItems.objects.create(cart=cart, product=product)

    if variant:
        variant = request.GET.get("variant")
        size_variant = SizeVariant.objects.get(size_name=variant)
        cart_item.size_variant = size_variant
        cart_item.save()

    # return HttpResponseRedirect(request.path_info)
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def remove_cart(request, cart_item_uid):
    try:
        cart_item = CartItems.objects.get(uid=cart_item_uid)
        cart_item.delete()
    except Exception as e:
        print(e)

    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def cart(request):
    # cart = Cart.objects.filter(is_paid = False , user = request.user)
    cart_obj = Cart.objects.filter(is_paid=False, user=request.user)
    if request.method == "POST":
        coupon = request.POST.get("coupon")
        coupon_obj = Coupon.objects.filter(coupon_code__icontains=coupon)
        if not coupon_obj.exists():
            messages.error(request, "Invalid Coupon")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if coupon:
            messages.warning(request, "Coupon Aleardy Exists.")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if cart_obj.get_cart_total() < coupon_obj[0].minimum_amount:
            messages.warning(
                request,
                f"Amount Should be greater than { coupon_obj[0].minimum_amount }",
            )
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        if coupon_obj[0].is_expired:
            messages.warning(request, f"Coupon Expired")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

        cart_obj.coupon = coupon_obj[0]
        cart_obj.save()
        messages.success(request, "Coupon Applied")
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

    context = {"cart": cart_obj}
    return render(request, "cart/cart.html", context)


def remove_coupon(request, cart_id):
    cart = Cart.objects.get(uid=cart_id)
    cart.coupon = None
    cart.save()
    messages.success(request, "Coupon Removed")
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
