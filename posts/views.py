from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post


def index(request):
    posts = Post.objects.filter(visible=True)
    if request.user.has_perm('posts.view_hidden'):
        posts = Post.objects.all()

    return render(request, 'posts/index.html', {
        'posts': posts,
        'top_posts': posts.filter(top_post=True),
    })


def post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if not post.visible and not request.user.has_perm('posts.view_hidden'):
        raise Http404("Post not found")

    return render(request, 'posts/post.html', {
        'post': post
    })
