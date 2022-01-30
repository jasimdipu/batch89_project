from os import name
import re
from django.shortcuts import render

from shop.models import Category, Product

# Create your views here.


def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'home.html', context)
