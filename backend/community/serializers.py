from rest_framework import serializers
from .models import Board, Favorite, Article, Comment
from accounts.serializers import UserSerializer, UserListSerializer


class BoardSerializer(serializers.ModelSerializer):
    user = serializers.IntegerField(source='user.id', required=False)
    class Meta:
        model = Board
        fields = '__all__'


class BoardListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'title']


class ArticleSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=False)
    like_users_count = serializers.SerializerMethodField()
    def get_like_users_count(self, obj):
        return obj.like_users.count()
    class Meta:
        model = Article
        fields = ['id', 'user', 'title', 'content', 'created_at', 'updated_at', 'like_users_count']


class ArticleCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    board = BoardSerializer(required=False)
    class Meta:
        model = Article
        fields = ['title', 'content', 'user', 'board']


class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UserListSerializer(required=True)
    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_at', 'updated_at', 'user']


class ArticleDetailSerializer(serializers.ModelSerializer):
    comment_set = ArticleCommentSerializer(many=True)
    like_users_count = serializers.SerializerMethodField()
    def get_like_users_count(self, obj):
        return obj.like_users.count()
    class Meta:
        model = Article
        fields = ['id','title', 'content', 'created_at', 'updated_at', 'like_users_count', 'comment_set']


class CommentCreateSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    article = ArticleSerializer(required=False)
    class Meta:
        model = Comment
        fields = '__all__'