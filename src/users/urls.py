from rest_framework.routers import DefaultRouter

from .views import UsersViewSet

routers = DefaultRouter()
routers.register('', UsersViewSet)

urlpatterns = []

urlpatterns += routers.urls
