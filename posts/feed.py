from django.contrib.syndication.views import Feed
from .models import Post

class LatestPostsFeed(Feed):
    title = "Latest posts from Brettcvz.com"
    link = "/posts/"
    description = "I write on things that interest me: product management, startups, and general tech trends."

    def items(self):
        return Post.objects.order_by('-pubdate')[:5]

    def item_title(self, post):
        return post.title

    def item_description(self, post):
        return post.clean_preview()
