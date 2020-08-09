from django.urls import path, re_path

from . import views

app_name = "projects"

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<project_id>\d+)[-\w]*$', views.project, name='project'),
]
