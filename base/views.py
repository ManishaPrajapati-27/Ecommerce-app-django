from django.shortcuts import render

# Create your views here.


def index(request):
    template_name = "base/index.html"
    context = {}
    return render(request, template_name, context)

def shop(request):
    template_name = "base/shop.html"
    context = {}
    return render(request, template_name, context)

def about(request):
    template_name = "base/about.html"
    context = {}
    return render(request, template_name, context)

def contact(request):
    template_name = "base/contact.html"
    context = {}
    return render(request, template_name, context)
