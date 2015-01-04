from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pubdate', 'visible', 'on_front_page', 'top_post')
    list_filter = ('pubdate', 'visible', 'on_front_page', 'top_post')
