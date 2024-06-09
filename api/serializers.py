from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Group, Follow, Post, Comment, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', read_only=True)

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment

class GpoupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group

class FollowSerializer(serializers.ModelSerializer):

    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault()
     )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username'
     )

    class Meta:
        fields = ('id','user', 'following')
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'following',),
            )
        ]