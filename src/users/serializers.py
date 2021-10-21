import uuid
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from .models import NotificationFriendsUser

User = get_user_model()


class UserFriendSubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'image']


class UserSerializer(serializers.ModelSerializer):
    friends = UserFriendSubscriberSerializer(many=True)
    subscribers = UserFriendSubscriberSerializer(many=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'last_login', 'first_name',
            'last_name', 'country', 'city', 'birthday',
            'image', 'friends', 'subscribers', 'date_joined'
        ]


class CreateUserSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'password','image',
            'city', 'country', 'birthday',
        ]

    def create(self, validated_data):
        """
        Create new user and create notification table for him
        """
        notification = NotificationFriendsUser.objects.create()
        notification.save()
        validated_data['username'] = uuid.uuid4()
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['notifications'] = notification
        return User.objects.create(**validated_data)


class FriendNotifications(serializers.Serializer):
    id_user = serializers.CharField()
