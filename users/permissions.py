def is_admin(user):
    """
    Check if user is an admin.
    """

    return (
        hasattr(user, "profile")
        and user.profile.role == "admin"
    )


def is_manager(user):
    """
    Check if user is a manager.
    """

    return (
        hasattr(user, "profile")
        and user.profile.role == "manager"
    )


def is_admin_or_manager(user):
    """
    Check if user is admin or manager.
    """

    return (
        hasattr(user, "profile")
        and user.profile.role in [
            "admin",
            "manager"
        ]
    )