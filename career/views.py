from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Career
from .forms import CareerForm


def get_careers(request):
    careers = Career.objects.all().order_by('-published_date')
    conexts = {'careers': careers}
    return render(request, 'careerlist.html', conexts)


def get_career_details(request, id):
    career = get_object_or_404(Career, pk=id)

    career.views += 1
    career.save()

    contexts = {'career': career}
    return render(request, 'career_details.html', contexts)


@login_required
def add_or_edit_career(request, pk=None):
    '''Add career form page'''
    career = get_object_or_404(Career, pk=pk) if pk else None
    if request.method == "POST":
        form = CareerForm(request.POST, request.FILES, instance=career)
        if form.is_valid():
            career = form.save()
            return redirect(get_career_details, career.pk)
    else:
        form = CareerForm(instance=career)
    return render(request, 'blogpostform.html', {'form': form})
