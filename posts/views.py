from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Post
from .forms import BlogPostForm
from comments.models import Comment
from comments.forms import CommentForm


def get_blog(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')

    # pagination
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    pagination_posts = paginator.get_page(page)

    return render(request, "blogposts.html", {'posts': posts, 'pagination_posts': pagination_posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    comments = Comment.objects.all()
    comment_list = []

    for comment in comments:
        comment_list = Comment.objects.all().order_by(
            '-pub_date').filter(post_id=post.pk)

    # add comment
    form = CommentForm(request.POST)

    user = request.user
    if form.is_valid() and user.is_authenticated:
        content = form.cleaned_data['content']
        comment = Comment()
        comment.post_id = post.id
        comment.content = content
        comment.save()
        return HttpResponseRedirect(reverse('post_detail', args=(post.id,)))

    return render(request, "postdetail.html", {'post': post, 'comments': comments, 'comment_list': comment_list, 'form': form})


def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})
