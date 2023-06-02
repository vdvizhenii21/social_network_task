from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Like

User = get_user_model()

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'text', 'pub_date', 'likes_count')

    def get_likes_count(self, obj):
        return obj.likes.count()        


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'user', 'post')
        read_only_fields = ('post','user')
    
    def create(self, validated_data):
        post = validated_data['post']
        user = validated_data['user']
        if Like.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError('You alredy liked this post')
        like = Like.objects.create(post=post, user=user)
        return like
