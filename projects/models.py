from django.db import models
from django.core.urlresolvers import reverse
import datetime
import re


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=255)
    image = models.URLField()
    pubdate = models.DateField(auto_now_add=True, editable=True)
    visible = models.BooleanField(default=True)
    content = models.TextField()

    #Show this project on the homepage
    on_front_page = models.BooleanField(default=False)

    class Meta:
        ordering = ['-pubdate']

    def publish(self):
        self.pubdate = datetime.date.today()
        self.visible = True
        self.save()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("projects:project", kwargs={'project_id': str(self.id)}) + "-" + self.title_slug()

    def title_slug(self):
        #Remove things other than word characters and spaces
        base = re.sub(r"[^\w ]", '', self.title)
        return base.replace(" ", "-").lower()
