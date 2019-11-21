from django.shortcuts import render


def get_experiences(request):
    return render(request, 'experiences.html')
