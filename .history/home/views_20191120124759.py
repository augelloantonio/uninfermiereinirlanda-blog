from django.shortcuts import render, redirect
from products.models import Product, Category
from django.db.models import Avg, F, Count


def index(request):
    return render(request, "index.html")


def contact_us(request):
    '''Contact Us view'''
    return render(request, 'contact.html')
