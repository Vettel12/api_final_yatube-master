from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet, CommentViewSet, FollowViewSet, GpoupViewSet

from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )

router = DefaultRouter()

router.register(r'posts', PostViewSet, basename='post')
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments')
router.register(r'follow', FollowViewSet, basename='follow')
router.register(r'group', GpoupViewSet, basename='group')
    
urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]