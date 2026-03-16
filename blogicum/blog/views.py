from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def index(request):
    """Главная страница со всеми постами."""
    post_list = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    ).order_by('-pub_date')[:5]

    context = {
        'post_list': post_list,
    }
    return render(request, 'blog/index.html', context)


def post_detail(request, id):
    """Страница отдельного поста."""
    post = get_object_or_404(
        Post,
        pk=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {
        'post': post,
    }
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    """Страница с постами по категориям."""
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=timezone.now(),
    ).order_by('-pub_date')

    context = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
