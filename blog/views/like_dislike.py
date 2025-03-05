from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from blog.models import Post


@login_required
def toggle_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
        post.dislikes.remove(request.user)  # Убираем дизлайк, если он есть

    return redirect('blog:post-detail', pk=post.pk)


@login_required
def toggle_dislike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
    else:
        post.dislikes.add(request.user)
        post.likes.remove(request.user)  # Убираем лайк, если он есть
    return redirect('blog:post-detail', pk=post.pk)