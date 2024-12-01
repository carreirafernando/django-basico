from django.http import Http404
from django.shortcuts import render

from app_blog.data import posts


# Create your views here.
def blog(request):

    context = {
        'text': 'Página do BLOG - 2',
        'title': 'Blog',
        'posts': posts
    }

    return render(request, 'global/blog.html', context)

def post(request, post_id):
    found_post = None

    for post in posts:
        if post['id'] == post_id:
            found_post = post
            break

    if found_post is None:
        raise Http404('Post não existe.')
    
    context = {
        'text': 'Página do BLOG - 2',
        'title': 'Posts',
        'post': found_post
    }
    return render(request, 'global/post.html', context)

def exemplo(request):

    context = {
        'text': 'Página do EXEMPLO - 2',
        'title': 'Exemplo'
    }

    return render(request, 'global/exemplo.html', context)