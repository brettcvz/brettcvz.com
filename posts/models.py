from django.db import models
from django.urls import reverse
import datetime
import re
import nh3


class Post(models.Model):
    title = models.CharField(max_length=100)
    pubdate = models.DateField(auto_now_add=True, editable=True)
    visible = models.BooleanField(default=True)
    content = models.TextField()

    #Show this post on the homepage
    on_front_page = models.BooleanField(default=False)
    #Show this post as a "top post"
    top_post = models.BooleanField(default=False)

    hacker_news_link = models.URLField(blank=True)

    class Meta:
        ordering = ['-pubdate']

    def publish(self):
        self.pubdate = datetime.date.today()
        self.visible = True
        self.save()

    def __str__(self):
        return self.title

    def preview(self):
        return self.content.partition("\n")[0]

    def clean_preview(self):
        return nh3.clean(self.preview(), strip=True)

    def get_absolute_url(self):
        return reverse("posts:post", kwargs={'post_id': str(self.id)}) + "-" + self.title_slug()

    def title_slug(self):
        #Remove things other than word characters and spaces
        base = re.sub(r"[^\w ]", '', self.title)
        return base.replace(" ", "-").lower()
