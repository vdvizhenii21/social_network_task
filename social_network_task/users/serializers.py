from rest_framework import serializers
from .models import UserActivity
from django.contrib.auth import get_user_model

User = get_user_model()
   

class CustomUserSerializer(serializers.ModelSerializer):

    last_login = serializers.SerializerMethodField(read_only=True)
    last_request = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            'email',
            'id',
            'username',
            'last_login',
            'last_request'
        )
    
    def get_last_login(self, user_object):
        return user_object.last_login

    def get_last_request(self, user_object):
        return user_object.useractivity.last_request