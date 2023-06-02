from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

app_name = "usersactivity"

router = DefaultRouter()
router.register("usersactivity", CustomUserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("djoser.urls")),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
