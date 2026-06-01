from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MessageForm
from .models import Message


@login_required
def inbox(request):
    """
    Display messages received by the logged-in user.
    """

    messages_list = Message.objects.filter(
        receiver=request.user,
        is_archived=False
    )

    return render(
        request,
        "messaging/inbox.html",
        {"messages_list": messages_list}
    )


@login_required
def sent_messages(request):
    """
    Display messages sent by the logged-in user.
    """

    messages_list = Message.objects.filter(
        sender=request.user
    )

    return render(
        request,
        "messaging/sent_messages.html",
        {"messages_list": messages_list}
    )


@login_required
def message_detail(request, pk):
    """
    Display a single message.

    Users can only view messages they sent or received.
    """

    message = get_object_or_404(
        Message,
        pk=pk
    )

    if message.receiver != request.user and message.sender != request.user:
        messages.error(request, "You do not have permission to view this message.")
        return redirect("inbox")

    if message.receiver == request.user and not message.is_read:
        message.is_read = True
        message.save()

    return render(
        request,
        "messaging/message_detail.html",
        {"message": message}
    )


@login_required
def send_message(request):
    """
    Create and send a message from the logged-in user.
    """

    if request.method == "POST":
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()

            messages.success(request, "Message sent successfully.")
            return redirect("sent_messages")

    else:
        form = MessageForm()

    return render(
        request,
        "messaging/message_form.html",
        {"form": form}
    )


@login_required
def archive_message(request, pk):
    """
    Archive a received message.
    """

    message = get_object_or_404(
        Message,
        pk=pk,
        receiver=request.user
    )

    message.is_archived = True
    message.save()

    messages.success(request, "Message archived.")
    return redirect("inbox")
