from django.http import JsonResponse
from django.shortcuts import  get_object_or_404
from django.contrib.auth.decorators import login_required

from blog.models import Post
@login_required
def toggle_bookmark(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
        bookmarked = True
        context ={
            'bookmarked': bookmarked,
            'bookmarked_count': post.bookmarks.count(),
        }


    return JsonResponse(context)