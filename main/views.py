from django.shortcuts import render
from datetime import datetime
from main.models import Contact
from products.models import *
from account.models import *
from django.contrib import messages
import requests


# Create your views here.

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def soap(request):
    prods=requests.get("http://ecommercesarthak.herokuapp.com//api/products").json()
    soap_prod=[]
    for prod in prods:
        if prod['category']['category_name']=="Soap":
            soap_prod.append(prod)
    return render(request,'soap.html',{'prods' : soap_prod})

def shampoo(request):
    return render(request,'shampoo.html')

def oil(request):
    return render(request,'oil.html')

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        phonenumber=request.POST.get('phonenumber')
        email=request.POST.get('email')
        desc=request.POST.get('desc')
        contact=Contact(name=name,email=email,phonenumber=phonenumber,desc=desc,date= datetime.today())
        contact.save()
        messages.success(request, 'We have recieved your details. We will contact you shortly.')
    return render(request,'contact.html')

def register(request):

    return render(request,'register.html')

def login(request):
    
    return render(request,'login.html')

def search(request):
    search_prods=requests.get("http://127.0.0.1:8000/api/products").json()
    if request.method == "POST":
        searched=request.POST.get('searched')
        search_prod=[]
        for i in search_prods:
            if i['product_name']==searched:
                search_prod.append(i)
        return render(request,'search.html',{'searched' : searched,'search_prods': search_prod})

    else:
        
        return render(request,'search.html')

def cart(request):
    return render(request,'cart.html')

def changepassword(request):
    return render(request,'changepassword.html')