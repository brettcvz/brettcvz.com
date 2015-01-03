from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^about/$', 'website.views.about', name='about'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^projects/', include('projects.urls', namespace='projects')),

    url(r'^admin/', include(admin.site.urls)),
)
