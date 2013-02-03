from models import Post, Category, Piece
from django.contrib import admin
from django.template.defaultfilters import slugify

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': (slugify('title'),), 'author':('author',)}
    list_display = ('title', 'author', 'time')
    search_fields = ('author', 'time')
    list_filter = ('time',)
    fields = ('title', 'author', 'body_markdown', 'description', 'time', 'category', 'slug')
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Piece)

