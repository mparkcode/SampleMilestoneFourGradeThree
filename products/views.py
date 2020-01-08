from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Game, Console, Brand
from news.models import Article
import http.client
import urllib.request
import urllib.error
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    games = Game.objects.order_by('?')[:4]
    article = Article.objects.order_by('?')[:1]
    return render(request, "products/index.html", {"games":games, 'article': article})
    
def all_brands(request):
    brands = Brand.objects.all().order_by('-name')
    return render(request, "products/all_brands.html", {"brands":brands})
    
def show_consoles(request, brand):
    brand = get_object_or_404(Brand, name=brand)
    consoles = Console.objects.filter(brand = brand).order_by('console_type')
    return render(request, "products/show_consoles.html", {'consoles':consoles, 'brand':brand})

    
def show_games(request, console):
    console_type = Console.objects.get(console_type=console)
    games=Game.objects.filter(console=console_type).order_by('title')
    return render(request, "products/show_games.html", {"games":games, "console": console_type})
    
