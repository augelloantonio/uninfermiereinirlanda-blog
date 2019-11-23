from django.shortcuts import render, redirect


def index(request):
    '''Index view'''
    return render(request, "index.html")


'''
NMBI Views
'''


def nmbi_view(request):
    '''NMBI page view'''
    return render(request, 'nmbi/nmbi.html')


def la_registrazione_view(request):
    '''View of the page La registrazione'''
    return render(request, 'nmbi/registrazione.html')


def application_view(request):
    '''View of the page application'''
    return render(request, 'nmbi/application.html')


def documenti_view(request):
    '''View of the page documenti necessari'''
    return render(request, 'nmbi/documenti.html')


def passi_finali_view(request):
    '''View of the page documenti necessari'''
    return render(request, 'nmbi/stepfinali.html')


'''
Contact Form View
'''


def contact_us(request):
    '''Contact Us view'''
    return render(request, 'contact.html')
