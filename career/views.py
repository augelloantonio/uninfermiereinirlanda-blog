from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from .models import Career
from .forms import CareerForm


def get_careers(request):
    careers = Career.objects.all().order_by('-published_date')
    conexts = {'experiences': experiences}
    return render(request, 'careerlist.html', conexts)


def get_career_details(request, id):
    career = get_object_or_404(Career, pk=id)

    career.views += 1
    career.save()

    contexts = {'career': career}
    return render(request, 'career_details.html', contexts)


@login_required
def add_career(request):
    '''Add experience form page'''
    form = CareerForm()
    return render(request, 'addcareer.html', {'form': form})
