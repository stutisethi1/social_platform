from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import FriendRequest
from notifications.models import Notification

def send_request(request, user_id):
    receiver = User.objects.get(id=user_id)
    sender = request.user

    if sender != receiver:
        FriendRequest.objects.create(sender=sender, receiver=receiver)

        # Create notification
        Notification.objects.create(
            sender=sender,
            receiver=receiver,
            message=f"{sender.username} sent you a friend request"
        )

    return redirect('home')


def accept_request(request, request_id):
    fr = FriendRequest.objects.get(id=request_id)
    fr.is_accepted = True
    fr.save()

    return redirect('home')