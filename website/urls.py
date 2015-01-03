from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'website.views.home', name='home'),
    url(r'^about/$', 'website.views.about', name='about'),
    url(r'^posts/', include('posts.urls', namespace='posts')),
    url(r'^projects/', include('projects.urls', namespace='projects')),

    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
