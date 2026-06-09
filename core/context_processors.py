from messaging.models import Message


def unread_messages(request):
    """
    Return unread message count.
    """

    if request.user.is_authenticated:

        count = Message.objects.filter(
            receiver=request.user,
            is_read=False,
            is_archived=False
        ).count()

        return {
            "unread_message_count": count
        }

    return {
        "unread_message_count": 0
    }