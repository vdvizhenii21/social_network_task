from .models import UserActivity
from django.utils import timezone

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            user_activity, created = UserActivity.objects.get_or_create(user=request.user)
            user_activity.last_request = timezone.now()
            user_activity.save()

        return response
