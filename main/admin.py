from models import Post, Category
from django.contrib import admin
from django.template.defaultfilters import slugify

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('title'),)}

admin.site.register(Post)
admin.site.register(Category)

