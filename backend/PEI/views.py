from django.http import JsonResponse
from django.shortcuts import render

from .models import *

# Create your views here.

def GetProducts(request):
    data = list(Product.objects.values())
    return JsonResponse({'data' : data})

def GetProduct(request,id):
    data = list(Product.objects.filter(id=id).values())
    return JsonResponse({'data' : data})

def GetCart(req):
    data = list(Product.objects.filter(inCart__gt=0).values())
    return JsonResponse({'data' : data})

def addCart(req,id):
    item = Product.objects.get(id=id)
    item.inCart += 1
    item.save()
    return JsonResponse(status=200,data={})

def rmCart(req,id):
    item = Product.objects.get(id=id)
    item.inCart = 0
    item.save()
    return JsonResponse(status=200,data={})