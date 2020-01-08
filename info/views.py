# info views
from django.shortcuts import render, redirect
from .forms import QuestionForm

# Create your views here.
def contact(request):
    form = QuestionForm()
    return render(request, 'info/contact.html', {"form": form})
    
def shipping(request):
    return render(request, 'info/shipping.html')
    
def faq(request):
    return render(request, 'info/faq.html')