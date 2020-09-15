from rest_framework import serializers
from .models import Board, Favorite, Article, Comment
from accounts.serializers import UserSerializer


class BoardSerializer(serializers.ModelSerializer):
  user = serializers.IntegerField(source='user.id', required=False)
  class Meta:
    model = Board
    fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  class Meta:
    model = Article
    fields = '__all__'


class ArticleCreateSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  board = BoardSerializer(required=False)
  class Meta:
    model = Article
    fields = ['title', 'content', 'user', 'board']


class ArticleCommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = ['id', 'content', 'created_at', 'updated_at', 'user']


class ArticleDetailSerializer(serializers.ModelSerializer):
  comment_set = ArticleCommentSerializer(many=True)
  class Meta:
    model = Article
    fields = ['id','title', 'content', 'created_at', 'updated_at', 'like_user', 'comment_set']


class CommentCreateSerializer(serializers.ModelSerializer):
  user = UserSerializer(required=False)
  article = ArticleSerializer(required=False)
  class Meta:
    model = Comment
    fields = '__all__'