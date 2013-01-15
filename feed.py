from django.contrib.syndication.views import Feed
from main.models import Post

class theFeed(Feed):
    title = 'matts@codecave:~$'
    link = ''
    description = ''


    def items(self):
        return Post.objects.order_by('-time')[:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description

    def item_link(self, item):
        return item.get_absolute_url()
