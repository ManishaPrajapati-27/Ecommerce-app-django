from django.shortcuts import render
from django.http import HttpResponseRedirect
from products.models import Product

# Create your views here.


def get_product(request, slug):
    # print('******')
    # print(request.user)
    # print('******')

    # print(request.user.account.get_cart_count)

    try:
        product = Product.objects.get(slug=slug)
        context = {"product": product}
        if request.GET.get("size"):
            size = request.GET.get("size")
            price = product.get_product_by_size(size)
            context["selected_size"] = size
            context["updated_price"] = price
            print(price)

        return render(request, "product/product.html", context=context)

    except Exception as e:
        print(e)


# link of product.html = localhost:8000/product/s,jhgs
