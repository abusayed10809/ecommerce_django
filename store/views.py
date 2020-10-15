from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def store(request):
    context = {
        "name": 'coffee',
        "price": '1400',
    }
    return render(request, 'store.html', context)

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')