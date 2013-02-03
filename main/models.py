from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.sitemaps import Sitemap

class Category(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse('views.category', args=[str(self.name)])

    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=160)
    author = models.CharField(max_length=100, default='Matt')
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

    def __unicode__(self):
        return self.title

class Piece(models.Model):
    title = models.CharField(max_length=140)
    short = models.CharField(max_length=240)
    body = models.TextField(blank=True, null=True)
    body_markdown = models.TextField()
    link = models.CharField(max_length=100)
    thumbnail = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)
    slug = models.SlugField(max_length=120, unique=True)

    class Meta:
        ordering = ['-time']

    def get_absolute_url(self):
        return reverse('views.piece', args=[str(self.slug)])

    def save(self):
        import markdown
        self.body = markdown.markdown(self.body_markdown)
        super(Piece, self).save()

    def __unicode__(self):
        return self.title
