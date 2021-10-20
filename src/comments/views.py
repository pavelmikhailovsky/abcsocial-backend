from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Comment
from .serializers import CommentsSerializer


class CommentsViewSet(viewsets.GenericViewSet,
                      mixins.DestroyModelMixin):
    # for 'basename' in routers
    queryset = Comment.objects

    serializer_class = CommentsSerializer

    def get_queryset(self):
        return self.queryset.all()

    @action(detail=False, methods=['POST'], url_path='create-comment-profile')
    def create_comment_profile(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            # create comment
            ...
        return

    @action(detail=True, methods=['POST'], url_path='create-child-comment-profile')
    def create_child_comments_profile_user(self, request, *args, **kwargs):
        parent_comment_id = kwargs['pk']
        return

    @action(detail=False, url_path='list')
    def list_comments(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

















