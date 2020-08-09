from django.urls import path, re_path

from . import views
from . import feed

app_name = "posts"

urlpatterns = [
    path('', views.index, name='index'),
    path('rss', feed.LatestPostsFeed(), name='rss'),
    re_path(r'^(?P<post_id>\d+)[-\w]*$', views.post, name='post'),
]
