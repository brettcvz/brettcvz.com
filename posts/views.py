from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def index(request):
    return render(request, 'posts/index.html', {
        'posts': Post.objects.filter(visible=True),
        'top_posts': Post.objects.filter(visible=True, top_post=True),
    })


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not post.visible:
        raise Http404("Post not found")

    return render(request, 'posts/post.html', {
        'post': post
    })
