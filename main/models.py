from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

class Category(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

    def get_absulute_url(self):
        return reverse('views.category', args=[str(self.name)])

class Post(models.Model):
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=100)
    body = models.TextField(blank=True, null=True)
    body_markdown = models.TextField()
    description = models.TextField(blank=True, null=True)
    time = models.DateTimeField(default=datetime.now)
    category = models.ForeignKey(Category)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta: 
        ordering = ['-time']

    def get_absolute_url(self):
        return reverse('views.details', args=[str(self.time.year), str(self.time.month), str(self.time.day), str(self.slug)])

    def save(self):
        import markdown
        self.body = markdown.markdown(self.body_markdown)
        super(Post, self).save()
