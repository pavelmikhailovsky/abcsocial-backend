from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins, status, parsers
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, CreateUserSerializer, FriendNotifications
from .pagination import CustomPageNumberPagination

User = get_user_model()


class UsersViewSet(viewsets.GenericViewSet, mixins.DestroyModelMixin):
    queryset = User.objects.all()
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def perform_destroy(self, instance):
        """
        Override default method perform_destroy on delete instance
        """
        instance.is_active = False
        instance.save()

    def get_serializer_class(self):
        if self.action == 'list_users':
            return UserSerializer
        elif self.action == 'create_user':
            return CreateUserSerializer
        elif self.action == 'friend_notifications':
            return FriendNotifications

    @action(detail=False, url_path='list')
    def list_users(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        self.pagination_class = CustomPageNumberPagination
        page = self.paginate_queryset(queryset)
        # TODO: show only is_active = True users

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], url_path='create')
    def create_user(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'status': 'created'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['POST'], url_path='friend-notifications')
    def friend_notifications(self, request, *args, **kwargs):
        """
        Accept id as user id
        """
        id_notification_table = self.get_serializer(request.data)

        try:
            user = User.objects.get(id=int(id_notification_table.data.get('id_user')))
        except User.DoesNotExist:
            return Response({'status': 'user is does not exist'}, status=status.HTTP_404_NOT_FOUND)
        else:
            number_notifications = user.notifications.notification.count()
            return Response({'number_of_notifications': f'{number_notifications}'}, status=status.HTTP_200_OK)












