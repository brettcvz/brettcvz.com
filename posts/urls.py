from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'posts.views.index', name='index'),
    url(r'^(?P<post_id>\d+)[-\w]*$', 'posts.views.post', name='post'),
)
