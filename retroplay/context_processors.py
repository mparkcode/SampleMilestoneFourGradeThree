from django.shortcuts import render
from django.http import HttpResponse
from products.models import Brand, Console
from cart.utils import get_cart_items_and_total

def get_brands(request):
    brands = Brand.objects.all().order_by('-name')
    return{"all_brands":brands}
    
def get_consoles(request):
    consoles = Console.objects.all().order_by('console_type')
    return{"all_consoles":consoles}
    
def item_quantity(request):
    cart = request.session.get('cart', {})
    context =  get_cart_items_and_total(cart)
    return context