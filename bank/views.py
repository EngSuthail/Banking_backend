from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse 
from .models import Customer 
 
def customer_list(request): 
    data = list(Customer.objects.values()) 
    return JsonResponse(data, safe=False) 
