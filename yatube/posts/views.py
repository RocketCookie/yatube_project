from django.shortcuts import get_object_or_404, render
from .models import Post, Group


QUANTITY_POSTS = 10


def index(request):
    posts = Post.objects.select_related('author', 'group')[:QUANTITY_POSTS]
    return render(request, 'posts/index.html', {'posts': posts, })


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.select_related('author')[:QUANTITY_POSTS]
    return render(request, 'posts/group_list.html',
                  {'group': group, 'posts': posts, })
