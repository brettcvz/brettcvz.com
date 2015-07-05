from django.conf.urls import patterns, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'projects.views.index', name='index'),
    url(r'^(?P<project_id>\d+)[-\w]*$', 'projects.views.project', name='project'),
)
