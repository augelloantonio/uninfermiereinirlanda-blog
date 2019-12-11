from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from .models import Experience
from comments.models import Comment
from comments.forms import CommentForm
from .forms import ExperienceForm


def get_experiences(request):
    experiences = Experience.objects.all().order_by('-published_date')
    conexts = {'experiences': experiences}
    return render(request, 'experiences.html', conexts)


def get_experience_details(request, id):
    experience = get_object_or_404(Experience, pk=id)

    experience.views += 1
    experience.save()

    comments = Comment.objects.all()
    comment_list = []

    for comment in comments:
        comment_list = Comment.objects.all().order_by(
            '-pub_date').filter(experience__id=experience.id)

    # add comment
    form = CommentForm(request.POST)
    user = request.user

    if form.is_valid() and user.is_authenticated:
        content = form.cleaned_data['content']
        comment = Comment()
        comment.experience_id = experience.id
        comment.content = content
        comment.save()
        return HttpResponseRedirect(reverse('get_experience_details', args=(experience.id,)))

    contexts = {'experience': experience,
                'form': form,
                'comment_list': comment_list}

    return render(request, 'experience_details.html', contexts)


@login_required
def add_or_edit_experience(request, pk=None):
    '''Add career form page'''
    experience = get_object_or_404(Experience, pk=pk) if pk else None
    if request.method == "POST":
        form = ExperienceForm(request.POST, request.FILES, instance=experience)
        if form.is_valid():
            experience = form.save()
            return redirect(get_experience_details, experience.pk)
    else:
        form = ExperienceForm(instance=experience)
    return render(request, 'addexperience.html', {'form': form})
