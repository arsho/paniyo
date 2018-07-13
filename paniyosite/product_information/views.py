from django.shortcuts import render
from django.http import HttpResponse

from .services import get_all_products

def index(request):
    products = get_all_products()
    context = {'products': products}
    return render(request, 'product_information/index.html', context)