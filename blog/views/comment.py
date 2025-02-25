from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(
                owner=request.user,
                post=post,
                content=content
            )
            return redirect('blog:post-detail', pk=pk)
    return redirect('blog:post-detail', pk=pk)

@login_required
def delete_comment(request,pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog:post-detail', pk=post_pk)
