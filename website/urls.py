from django.urls import include, path
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # Examples:
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('favorites/', views.favorites, name='favorites'),
    path('posts/', include('posts.urls', namespace='posts')),
    path('projects/', include('projects.urls', namespace='projects')),

    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
