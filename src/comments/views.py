from rest_framework import viewsets

from .models import Comment
from .serializers import CommentsSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    # for 'basename' in routers
    queryset = Comment.objects

    serializer_class = CommentsSerializer

    def get_queryset(self):
        return Comment.objects.all()
