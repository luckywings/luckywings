from django.shortcuts import render
from . models import Product

# Create your views here.


def index(request):
    return render(request,"index.html")

def shop(request):
    return render(request,"shop.html")


def why(request):
    return render(request,"why.html")


def contact(request):
    return render(request,"contact.html")

def testimonial(request):
    return render(request,"testimonial.html")


def login(request):
    return render(request,"login.html")


def product(request):
    return render(request,"product.html")

def allproduct(request):
    product=Product.object.all()
    return render(request,"allproduct.html",{"product":product})

def product_de(request):
    return render(request,"product_de.html")