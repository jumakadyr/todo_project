from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.models import Post


@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    context = {
        'liked': liked,
        'liked_count':post.likes.count(),
    }
    return JsonResponse(context)

@login_required
def toggle_dislike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True
    context = {
        'disliked': disliked,
        'disliked_count':post.dislikes.count(),
    }
    return JsonResponse(context)