from django.contrib.auth import get_user_model
from .serializers import CustomUserSerializer
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

User = get_user_model()

class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [AllowAny]