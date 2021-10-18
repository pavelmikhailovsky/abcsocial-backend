from rest_framework import serializers

from .models import Comment


class CommentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'text']


class CommentsSerializer(serializers.ModelSerializer):
    parent = CommentsDetailSerializer(many=True)

    class Meta:
        model = Comment
        fields = ['id', 'text', 'parent']

