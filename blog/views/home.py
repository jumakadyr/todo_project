from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from blog.forms import Post, Category

@login_required
def home(request):
    query = request.GET.get('q', '')
    sort_by = request.GET.get('sort', '-updated_at')

    posts = Post.objects.all()

    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(content__icontains=query) |
            Q(owner__first_name=query) |
            Q(owner__last_name=query)
        )

    posts = posts.order_by(sort_by)

    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
        'query': query,
        'sort_by': sort_by,
    }
    return render(request, 'blog/index.html', context)
