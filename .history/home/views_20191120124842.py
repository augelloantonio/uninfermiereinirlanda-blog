from django.shortcuts import render, redirect


def index(request):
    '''Index view'''
    return render(request, "index.html")


def contact_us(request):
    '''Contact Us view'''
    return render(request, 'contact.html')
