from django.conf.urls import url

import views
import feed

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^rss$', feed.LatestPostsFeed(), name='rss'),
    url(r'^(?P<post_id>\d+)[-\w]*$', views.post, name='post'),
]
