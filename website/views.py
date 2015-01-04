from django.shortcuts import render

from posts.models import Post


def home(request):
    return render(request, 'home.html', {
        "top_posts": Post.objects.filter(visible=True, on_front_page=True)
    })


def about(request):
    return render(request, 'about.html')
