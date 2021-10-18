from django.urls import path, include

urlpatterns = [
    path('comments/', include('src.comments.urls')),
]

