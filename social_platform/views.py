from django.shortcuts import render, redirect
from posts.models import Post
from django.contrib.auth.models import User
from friends.models import FriendRequest
from notifications.models import Notification

def home(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('content')
            image = request.FILES.get('image')

            Post.objects.create(
                author=request.user,
                content=content,
                image=image
            )

        return redirect('home')

    
    posts = Post.objects.all()

   
    users = []
    requests = []
    notifications = []

    if request.user.is_authenticated:
        query = request.GET.get('q')

        if query:
            users = User.objects.filter(
                username__icontains=query
            ).exclude(id=request.user.id)
        else:
            users = User.objects.exclude(id=request.user.id)

        requests = FriendRequest.objects.filter(
            receiver=request.user,
            is_accepted=False
        )

        notifications = Notification.objects.filter(
            receiver=request.user
        )

    return render(request, 'home.html', {
        'posts': posts,
        'users': users,
        'requests': requests,
        'notifications': notifications
    })