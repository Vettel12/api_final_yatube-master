from rest_framework import viewsets, permissions, filters
from .models import Post, Group, Comment, Follow
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, GpoupSerializer, CommentSerializer, FollowSerializer
from .permissions import IsAuthorOrReadOnlyPermission

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]

    def get_queryset(self):
        group = self.request.query_params.get('group')
        if group is not None:
            queryset = Post.objects.filter(group=group)
            return queryset
        queruset = Post.objects.all()
        return queruset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class GpoupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GpoupSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]
    
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission, permissions.IsAuthenticated]

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = [IsAuthorOrReadOnlyPermission]

    filter_backends = [filters.SearchFilter]
    filterset_fields = ('user__username',)
    search_fields = ('=user__username', '=following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)