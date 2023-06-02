from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Post
from rest_framework import permissions
from .serializers import PostSerializer, LikeSerializer
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Like
from django.contrib.auth import get_user_model

User = get_user_model()

class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    serializer_class = LikeSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, id=self.kwargs['post_id'])
        return post.likes.all()

    def perform_create(self, serializer):
        id=self.kwargs['post_id']
        post = get_object_or_404(Post, id=id)
        user = User.objects.get(id=self.request.user.id)
        print(user.last_login)
        serializer.save(user=self.request.user, post=post)


class LikesCountAPIView(APIView):
    def get(self, request):
        start_date = request.query_params.get('date_from')
        end_date = request.query_params.get('date_to')
        queryset = Like.objects.filter(created_at__range=[start_date, end_date]).count()
        return Response(queryset)
