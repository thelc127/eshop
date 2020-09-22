from django.shortcuts import render
from django.http import HttpResponse
from .models.product import Product


# Create your views here.
def index(request):
	p = Product.get_all_products()
	#return render(request, 'orders/order.html')
	return render(request, 'base.html', {'products' : p})
	