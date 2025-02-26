from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.models import Category

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories':categories})

@login_required
def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category_posts = category.posts.all()
    context = {
        'category_posts': category_posts,
        'category': category,
    }
    return render(request, 'blog/category_detail.html', context)










