from django.template.defaultfilters import title
from django.db.models import Q
from blog.models import Post
from django.shortcuts import render, redirect
from django.contrib import messages
from blog.forms import CreatePostForm

def index(request):
    if 'q' in request.GET and request.GET['q'] != '':
        posts = Post.objects.filter(
            Q(title__icontains = request.GET['q']) |
            Q(description__icontains=request.GET('q'))
            )
    else:
        posts = Post.objects.all()
    context = {
        'posts':posts,
    }

    return render(request, 'blog/index.html',context)

def add_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            post = Post(
                category = data['category'],
                owner = request.user,
                title = data['title'],
                decription = data['description'],
                content = data['content'],
                art_image = data['art_image']
            )
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('blog:index')
        context = {
            'form':CreatePostForm()
        }
        return render(request, 'blog/create_post.html', context)

    context = {
        'form': CreatePostForm()
    }
    return render(request, 'blog/create_post.html', context)