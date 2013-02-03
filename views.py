from django.shortcuts import render_to_response
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from main.models import *
from django.template import RequestContext

def index(request):
    all_posts = Post.objects.order_by('-time')
    paginator = Paginator(all_posts, 6)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    recent_posts = all_posts[:4]

    cats = Category.objects.all()

    template_data = {'posts':posts, 'recs':recent_posts, 'categories':cats}

    return render_to_response('index.html', template_data)


def category(request, category):
    cats = Post.objects.filter(category__name=category).order_by('-time')
    paginator = Paginator(cats, 4)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)

    cats = Category.objects.all()
    recent_posts = Post.objects.order_by('-time')[:4]

    template_data = {'posts':posts, 'recs':recent_posts, 'categories':cats}
    return render_to_response('index.html', template_data)


def details(request, year, month, day, title):
    post = Post.objects.get(slug=title)
    cats = Category.objects.all()
    recent_posts = Post.objects.order_by('-time')[:4]
    return render_to_response('post.html', {'post':post, 'recs':recent_posts,
         'categories':cats}, context_instance=RequestContext(request))


def about(request):
    cats = Category.objects.all()
    recent_posts = Post.objects.order_by('-time')[:4]
    about = Piece.objects.get(slug="about")
    return render_to_response('piece.html', {'recs':recent_posts,
         'categories':cats, 'piece':about})


def portfolio(request):
    all_pieces = Piece.objects.order_by('-time')
    paginator = Paginator(all_pieces, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        pieces = paginator.page(page)
    except:
        pieces = paginator.page(paginator.num_pages)

    recent_posts = Post.objects.order_by('-time')[:4]

    cats = Category.objects.all()

    template_data = {'pieces':pieces, 'recs':recent_posts, 'categories':cats}

    return render_to_response('portfolio.html', template_data)

def piece(request, title):
    piece = Piece.objects.get(slug=title)
    cats = Category.objects.all()
    recent_posts = Post.objects.order_by('-time')

    return render_to_response('piece.html', {'piece':piece, 'recs':recent_posts,
         'categories':cats})

