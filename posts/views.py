from django.shortcuts import redirect, get_object_or_404
from .models import Post, Comment

def like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.user in post.likes.all():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return redirect('home')


def add_comment(request, post_id):
    if request.method == "POST" and request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        content = request.POST.get('content')

        if content:
            Comment.objects.create(
                post=post,
                author=request.user,
                content=content
            )

    return redirect('home')