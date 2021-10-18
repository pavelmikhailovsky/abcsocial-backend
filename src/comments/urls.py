from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet

routers = DefaultRouter()
routers.register('', CommentsViewSet)

urlpatterns = []

urlpatterns += routers.urls
