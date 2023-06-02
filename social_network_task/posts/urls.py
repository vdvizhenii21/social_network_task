from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, LikeViewSet, LikesCountAPIView


router_v1 = DefaultRouter()
router_v1.register('posts', PostViewSet, basename='api_posts')
router_v1.register(
    r'likes/(?P<post_id>[^/.]+)',
    LikeViewSet,
    basename='api_likes'
)

urlpatterns = [
    path('api/posts/v1/', include(router_v1.urls)),
    path('api/analitics/', LikesCountAPIView.as_view(), name='likes-count'),
]