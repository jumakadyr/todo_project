from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

from blog.models import Post, Category


def home(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/index.html', context)



urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('account.urls', namespace="account")),
    path('blog/', include('blog.urls', namespace='blog'))
]
